FROM python:3.9.1-alpine3.13 as base

WORKDIR /app

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

# ENV LANG=C.UTF-8 # Already done in the python base image
# ENV PYTHONDONTWRITEBYTECODE=1 # Not a use case for this as we are using gunicorn

FROM base as build

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.4 \
    CRYPTOGRAPHY_DONT_BUILD_RUST=1

#install gcc
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# Setup the virtualenv
RUN python -m venv /venv

# Install Deps
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"
COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes -f requirements.txt --output requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl

FROM base as final

RUN apk add --no-cache libffi
COPY --from=build /venv /venv
COPY src/pex/*.py /app/
COPY entrypoint.sh /app/

ARG COMMIT_SHA=""
LABEL commit_sha=${COMMIT_SHA}
ENV COMMIT_SHA=${COMMIT_SHA}

CMD ["/app/entrypoint.sh"]
