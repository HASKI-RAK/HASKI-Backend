import logging
import os
from typing import Any

import requests

from utils import constants as cons

logger = logging.getLogger(__name__)


def _laac_base_url() -> str:
    return os.environ.get("LAAC_BASE_URL", "https://laac.haski.app/api/v1")


def _laac_verify_ssl() -> bool:
    return os.environ.get("LAAC_VERIFY_SSL", "true").lower() not in ("false", "0", "no")


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
