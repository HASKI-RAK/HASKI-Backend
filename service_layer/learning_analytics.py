import logging
import os
from typing import Any
from urllib.parse import parse_qs, urlparse

import requests

from utils import constants as cons

logger = logging.getLogger(__name__)


def _laac_base_url() -> str:
    return os.environ.get("LAAC_BASE_URL", "https://laac.haski.app/api/v1")


def _laac_verify_ssl() -> bool:
    return os.environ.get("LAAC_VERIFY_SSL", "false").lower() not in (
        "false",
        "0",
        "no",
    )


def _laac_headers() -> dict[str, str]:
    headers = {"Accept": "application/json"}

    bearer = (
        os.environ.get("LAAC_BEARER_TOKEN")
        or os.environ.get("LAAC_API_TOKEN")
        # LAAC provides a DEV_JWT helper; accept both names for flexibility
        or os.environ.get("LAAC_DEV_JWT")
        or os.environ.get("DEV_JWT")
    )
    api_key = os.environ.get("LAAC_API_KEY")

    if bearer:
        headers["Authorization"] = f"Bearer {bearer}"
    if api_key:
        headers["x-api-key"] = api_key

    return headers


def _laac_course_id(course_id: Any) -> str:
    return os.environ.get("MOODLE_COURSE_URL") + str(course_id)


def fetch_element_clicks(
    user_id: Any,
    course_id: Any | None = None,
    topic_id: Any | None = None,
) -> list[dict[str, Any]]:
    """
    Retrieve the LAAC `element-clicks` metric for a given user and context.

    Returns an empty list on any error to allow GA to continue with neutral defaults.
    """

    if user_id is None:
        return []

    params = {"userId": user_id}
    if course_id is not None:
        params["courseId"] = course_id
    if topic_id is not None:
        params["topicId"] = topic_id

    url = f"{_laac_base_url().rstrip('/')}/metrics/element-clicks"
    try:
        response = requests.get(
            url,
            params=params,
            headers=_laac_headers(),
            timeout=5,
            verify=_laac_verify_ssl(),
        )
        if response.status_code != 200:
            logger.warning(
                "LAAC element-clicks request failed: %s %s",
                response.status_code,
                response.text,
            )
            return []
        payload = response.json()
        return payload.get("result", {}).get("value", []) or []
    except (
        requests.RequestException,
        ValueError,
        KeyError,
    ) as exc:  # pragma: no cover - network/path errors are non-deterministic
        logger.warning("LAAC element-clicks request raised %s", exc)
        return []


def map_clicks_to_classification(
    clicks_payload: list[dict[str, Any]],
) -> dict[str, float]:
    """
    Convert LAAC response entries into a mapping keyed by internal LE classification.
    Values are the raw `dimensionScore` numbers supplied by LAAC.
    """
    scores: dict[str, float] = {}
    for entry in clicks_payload:
        type_code = entry.get("type")
        classification = cons.laac_type_to_classification.get(type_code)
        if not classification:
            continue
        score = entry.get("dimensionScore")
        if isinstance(score, (int, float)):
            scores[classification] = float(score)
    return scores


def get_click_scores_for_learning_path(
    user_id: Any,
    course_id: Any | None = None,
    topic_id: Any | None = None,
) -> dict[str, float]:
    """
    High-level helper to fetch and map click scores once per learning path calculation.
    Always returns a dictionary (possibly empty)\
        to signal the GA that the Clicks dimension
    should be present, even if LA data is missing.
    """
    raw_clicks = fetch_element_clicks(
        user_id=user_id, course_id=course_id, topic_id=topic_id
    )
    return map_clicks_to_classification(raw_clicks)


def map_items_to_record(items: list[dict]) -> dict[str, Any]:
    """
    Convert LAAC response entries into a mapping keyed by course ID.
    Values are the raw `score` numbers supplied by LAAC.
    """
    mapped: dict[str, Any] = {}
    fields = {"score", "maxScore", "timeSpent", "completedAt", "completionStatus"}

    for item in items:
        url = item.get("courseId") or item.get("elementId")
        if not url:
            continue

        element_id = parse_qs(urlparse(url).query).get("id", [None])[0]
        if element_id is None:
            continue

        present = {
            key: item[key] for key in fields if key in item and item[key] is not None
        }
        if not present:
            continue

        mapped[element_id] = (
            next(iter(present.values())) if len(present) == 1 else present
        )

    return mapped


def fetch_courses_scores(
    user_id: Any, since: Any | None = None, until: Any | None = None
) -> list[dict[str, int]]:
    """
    Retrieve the LAAC `course-total-score` metric for a given user and context.

    Returns an empty array on any error to allow the frontend\
        to continue with neutral defaults.
    """
    if user_id is None:
        return []

    params = {
        "userId": user_id,
    }

    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until

    url = f"{_laac_base_url().rstrip('/')}/metrics/courses-scores/results"
    try:
        response = requests.get(
            url,
            params=params,
            headers=_laac_headers(),
            timeout=20,
            verify=_laac_verify_ssl(),
        )
        if response.status_code != 200:
            logger.warning(
                "LAAC courses-scores request failed: %s %s",
                response.status_code,
                response.text,
            )
            return []
        payload = response.json()
        return payload.get("value", []) or []
    except (
        requests.RequestException,
        ValueError,
        KeyError,
    ) as exc:  # pragma: no cover - network/path errors are non-deterministic
        logger.warning("LAAC courses-scores request raised %s", exc)
        return []


def get_courses_scores(
    user_id: Any, since: Any | None = None, until: Any | None = None
) -> dict[str, int]:
    """
    High-level helper to fetch and map courses scores once per frontend request.
    Always returns a dictionary (possibly empty)\
        to signal the frontend that the courses scores
    should be present, even if LA data is missing.
    """
    courses_scores = fetch_courses_scores(user_id, since, until)
    print("courses_scores, (line 432 learning_analytics)", courses_scores)
    return map_items_to_record(courses_scores)


def fetch_courses_max_scores(
    user_id: Any, since: Any | None = None, until: Any | None = None
) -> list[dict[str, int]]:
    """
    Retrieve the LAAC `courses-max-scores` metric for a given user and context.

    Returns an empty array on any error to allow the frontend\
        to continue with neutral defaults.
    """
    if user_id is None:
        return []

    params = {
        "userId": user_id,
    }

    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until

    url = f"{_laac_base_url().rstrip('/')}/metrics/courses-max-scores/results"
    try:
        response = requests.get(
            url,
            params=params,
            headers=_laac_headers(),
            timeout=20,
            verify=_laac_verify_ssl(),
        )
        if response.status_code != 200:
            logger.warning(
                "LAAC courses-max-scores request failed: %s %s",
                response.status_code,
                response.text,
            )
            return []
        payload = response.json()
        return payload.get("value", []) or []
    except (
        requests.RequestException,
        ValueError,
        KeyError,
    ) as exc:  # pragma: no cover - network/path errors are non-deterministic
        logger.warning("LAAC courses-max-scores request raised %s", exc)
        return []


def get_courses_max_scores(
    user_id: Any, since: Any | None = None, until: Any | None = None
) -> dict[str, int]:
    """
    High-level helper to fetch and map courses max scores once per frontend request.
    Always returns a dictionary (possibly empty)\
        to signal the frontend that the courses max scores
    should be present, even if LA data is missing.
    """
    courses_max_scores = fetch_courses_max_scores(user_id, since, until)
    return map_items_to_record(courses_max_scores)


def fetch_courses_time_spent(
    user_id: Any, since: Any | None = None, until: Any | None = None
) -> list[dict[str, int]]:
    """
    Retrieve the LAAC `courses-time-spent` metric for a given user and context.

    Returns an empty array on any error to allow the frontend\
        to continue with neutral defaults.
    """

    if user_id is None:
        return []

    params = {
        "userId": user_id,
    }

    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until

    url = f"{_laac_base_url().rstrip('/')}/metrics/courses-time-spent/results"
    try:
        response = requests.get(
            url,
            params=params,
            headers=_laac_headers(),
            timeout=20,
            verify=_laac_verify_ssl(),
        )
        if response.status_code != 200:
            logger.warning(
                "LAAC course-time-spent request failed: %s %s",
                response.status_code,
                response.text,
            )
            return []
        payload = response.json()
        return payload.get("value", []) or []
    except (
        requests.RequestException,
        ValueError,
        KeyError,
    ) as exc:  # pragma: no cover - network/path errors are non-deterministic
        logger.warning("LAAC course-time-spent request raised %s", exc)
        return []


def get_courses_time_spent(
    user_id: Any, since: Any | None = None, until: Any | None = None
) -> dict[str, int]:
    """
    High-level helper to fetch and map courses time spent once per frontend request.
    Always returns a dictionary (possibly empty)\
        to signal the frontend that the courses time spent
    should be present, even if LA data is missing.
    """
    courses_time_spent = fetch_courses_time_spent(user_id, since, until)
    return map_items_to_record(courses_time_spent)


def fetch_user_last_elements(
    user_id: Any, since: Any | None = None, until: Any | None = None
) -> list[dict[str, Any]]:
    """
    Retrieve the LAAC `user-last-elements` metric for a given user and context.

    Returns an empty array on any error to allow the frontend\
        to continue with neutral defaults.
    """

    if user_id is None:
        return []

    params = {
        "userId": user_id,
    }

    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until

    url = f"{_laac_base_url().rstrip('/')}/metrics/user-last-elements/results"
    try:
        response = requests.get(
            url,
            params=params,
            headers=_laac_headers(),
            timeout=20,
            verify=_laac_verify_ssl(),
        )
        if response.status_code != 200:
            logger.warning(
                "LAAC course-last-elements request failed: %s %s",
                response.status_code,
                response.text,
            )
            return []
        payload = response.json()
        return payload.get("value", []) or []
    except (
        requests.RequestException,
        ValueError,
        KeyError,
    ) as exc:  # pragma: no cover - network/path errors are non-deterministic
        logger.warning("LAAC course-last-elements request raised %s", exc)
        return []


def get_user_last_elements(user_id: Any) -> list[dict[str, Any]]:
    """
    High-level helper to fetch user last elements once per frontend request.
    Always returns a list (possibly empty)\
        to signal the frontend that the user last elements
    should be present, even if LA data is missing.
    """
    user_last_elements = fetch_user_last_elements(user_id)
    return map_items_to_record(user_last_elements)


def fetch_course_elements_max_scores(
    user_id: Any, course_id: Any, since: Any | None = None, until: Any | None = None
) -> list[dict[str, Any]]:
    """
    Retrieve the LAAC `course-elements-max-scores` metric for a given user and course.
    Returns an empty array on any error to allow the frontend\
        to continue with neutral defaults.
    """

    if user_id is None or course_id is None:
        return []

    params = {
        "userId": user_id,
        "courseId": _laac_course_id(course_id),
    }

    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until

    url = f"{_laac_base_url().rstrip('/')}/metrics/course-elements-max-scores/results"

    try:
        response = requests.get(
            url,
            params=params,
            headers=_laac_headers(),
            timeout=20,
            verify=_laac_verify_ssl(),
        )
        if response.status_code != 200:
            logger.warning(
                "LAAC course-elements-max-scores request failed: %s %s",
                response.status_code,
                response.text,
            )
            return []
        payload = response.json()
        return payload.get("value", []) or []
    except (
        requests.RequestException,
        ValueError,
        KeyError,
    ) as exc:  # pragma: no cover - network/path errors are non-deterministic
        logger.warning("LAAC course-elements-max-scores request raised %s", exc)
        return []


def get_course_elements_max_scores(
    user_id: Any, course_id: Any, since: Any | None = None, until: Any | None = None
) -> dict[str, int]:
    """
    High-level helper to fetch and map course elements max scores\
        once per frontend request.
    Always returns a dictionary (possibly empty)\
        to signal the frontend that the course elements max scores
    should be present, even if LA data is missing.
    """
    course_elements_max_scores = fetch_course_elements_max_scores(
        user_id, course_id, since, until
    )
    return map_items_to_record(course_elements_max_scores)


def fetch_course_elements_best_attempts(
    user_id: Any,
    course_id: Any,
) -> list[dict[str, Any]]:
    """
    Retrieve the LAAC `course-elements-best-attempts` metric\
        for a given user and course.
    Returns an empty array on any error to allow the frontend\
        to continue with neutral defaults.
    """

    if user_id is None or course_id is None:
        return []

    params = {
        "userId": user_id,
        "courseId": _laac_course_id(course_id),
    }

    url = (
        f"{_laac_base_url().rstrip('/')}/metrics/course-elements-best-attempts/results"
    )

    try:
        response = requests.get(
            url,
            params=params,
            headers=_laac_headers(),
            timeout=20,
            verify=_laac_verify_ssl(),
        )
        if response.status_code != 200:
            logger.warning(
                "LAAC course-elements-best-attempts request failed: %s %s",
                response.status_code,
                response.text,
            )
            return []
        payload = response.json()
        return payload.get("value", []) or []
    except (
        requests.RequestException,
        ValueError,
        KeyError,
    ) as exc:  # pragma: no cover - network/path errors are non-deterministic
        logger.warning("LAAC course-elements-best-attempts request raised %s", exc)
        return []


def get_course_elements_best_attempts(user_id: Any, course_id: Any) -> dict[str, int]:
    """
    High-level helper to fetch and map course elements best attempts\
        once per frontend request.
    Always returns a dictionary (possibly empty)\
        to signal the frontend that the course elements best attempts
    should be present, even if LA data is missing.
    """
    course_elements_best_attempts = fetch_course_elements_best_attempts(
        user_id, course_id
    )
    print("course_elements_best_attempts, (line 532 learning_analytics)", course_elements_best_attempts)
    return map_items_to_record(course_elements_best_attempts)


def fetch_course_elements_time_spent(
    user_id: Any, course_id: Any, since: Any | None = None, until: Any | None = None
) -> list[dict[str, Any]]:
    """
    Retrieve the LAAC `course-elements-time-spent` metric for a given user and course.
    Returns an empty array on any error to allow the frontend\
        to continue with neutral defaults.
    """

    if user_id is None or course_id is None:
        return []

    params = {
        "userId": user_id,
        "courseId": _laac_course_id(course_id),
    }

    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until

    url = f"{_laac_base_url().rstrip('/')}/metrics/course-elements-time-spent/results"

    try:
        response = requests.get(
            url,
            params=params,
            headers=_laac_headers(),
            timeout=20,
            verify=_laac_verify_ssl(),
        )
        if response.status_code != 200:
            logger.warning(
                "LAAC course-elements-time-spent request failed: %s %s",
                response.status_code,
                response.text,
            )
            return []
        payload = response.json()
        return payload.get("value", []) or []
    except (
        requests.RequestException,
        ValueError,
        KeyError,
    ) as exc:  # pragma: no cover - network/path errors are non-deterministic
        logger.warning("LAAC course-elements-time-spent request raised %s", exc)
        return []


def get_course_elements_time_spent(
    user_id: Any, course_id: Any, since: Any | None = None, until: Any | None = None
) -> dict[str, int]:
    """
    High-level helper to fetch and map course elements time spent\
        once per frontend request.
    Always returns a dictionary (possibly empty)\
        to signal the frontend that the course elements time spent
    should be present, even if LA data is missing.
    """
    course_elements_time_spent = fetch_course_elements_time_spent(
        user_id, course_id, since, until
    )
    return map_items_to_record(course_elements_time_spent)


def fetch_course_last_elements(
    user_id: Any, course_id: Any, since: Any | None = None, until: Any | None = None
) -> list[dict[str, Any]]:
    """
    Retrieve the LAAC `course-last-elements` metric for a given user and course.
    Returns an empty array on any error to allow the frontend\
        to continue with neutral defaults.
    """

    if user_id is None or course_id is None:
        return []

    params = {
        "userId": user_id,
        "courseId": _laac_course_id(course_id),
    }

    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until

    url = f"{_laac_base_url().rstrip('/')}/metrics/course-last-elements/results"

    try:
        response = requests.get(
            url,
            params=params,
            headers=_laac_headers(),
            timeout=20,
            verify=_laac_verify_ssl(),
        )
        if response.status_code != 200:
            logger.warning(
                "LAAC course-last-elements request failed: %s %s",
                response.status_code,
                response.text,
            )
            return []
        payload = response.json()
        return payload.get("value", []) or []
    except (
        requests.RequestException,
        ValueError,
        KeyError,
    ) as exc:  # pragma: no cover - network/path errors are non-deterministic
        logger.warning("LAAC course-last-elements request raised %s", exc)
        return []


def get_course_last_elements(
    user_id: Any, course_id: Any, since: Any | None = None, until: Any | None = None
) -> dict[str, Any]:
    """
    High-level helper to fetch and map course last elements once per frontend request.
    Always returns a dictionary (possibly empty)\
        to signal the frontend that the course last elements
    should be present, even if LA data is missing.
    """
    course_last_elements = fetch_course_last_elements(user_id, course_id, since, until)
    return map_items_to_record(course_last_elements)
