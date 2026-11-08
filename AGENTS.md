## General

Use the tool calling functions given to you if needed.
Use context7 if unsure about syntax.

## Python

- Use python venv in the workspace folder.
- Always activate the venv before running code.
- For tests use `tox`.
- Always use black + isort + flake8 for formatting and linting (configs in `pyproject.toml`).

## Project quick facts

- Python 3.10, Flask REST API with layered architecture (domain/service/repositories).
- Formatter/lint stack is black + isort + flake8 (configs in `pyproject.toml`).
- JWT RS256 keys required at `keys/private.pem` and `keys/public.pem` (or set `JWT_KEYS_LOCATION`).
- App config comes from `.flaskenv` (template: `.flaskenv_template`).

## Common tasks

- Run dev server: `flask run` (after activating venv and loading `.flaskenv`).
- Tests directly: `tox`

## Architecture (concise)

- Entry: `entrypoints/flask_app.py` (Flask + CORS) registers blueprints in `entrypoints/endpoints` for LMS, user, course APIs; JSON error handling via `errors/`.
- Domain layer by concern: `domain/domainModel` (courses, topics, learning elements), `domain/learnersModel` (ILS questionnaire & characteristics), `domain/tutoringModel` (learning-path algorithms incl. GA), `domain/userAdministartion` (users/roles).
- Persistence: SQLAlchemy Core mappings live in `repositories/orm.py`; repository classes in `repositories/repository.py` used via Unit of Work in `service_layer/unit_of_work.py`.
- Service layer: `service_layer/services.py` holds use-cases (enrollment, learning element/topic assignment, learning path selection) and orchestrates repositories; LTI/OIDC helpers in `service_layer/lti`; crypto/JWT helpers in `service_layer/crypto`.
- Utilities: `utils/constants.py` for role strings; `utils/logger.py` sets logging.
