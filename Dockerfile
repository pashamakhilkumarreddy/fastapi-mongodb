ARG PYTHON_VERSION=3.12.4

FROM python:${PYTHON_VERSION} as build

WORKDIR /tmp

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:${PYTHON_VERSION}-alpine

WORKDIR /code

RUN addgroup -S appgroup && adduser -S python -G appgroup

RUN apk add --no-cache libffi openssl

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY --from=build /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./.env /code/.env

COPY ./app /code/app

RUN mkdir -p /code/static

RUN chown -R python:appgroup /code

USER python

ENV PORT=8080

EXPOSE $PORT

CMD ["sh", "-c", "uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port $PORT --workers 4"]