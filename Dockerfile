FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/app

RUN apk add --no-cache openssl-dev libffi-dev build-base postgresql-dev \
    && pip install pip --upgrade \
    && pip install pipenv

COPY app/Pipfile ./

RUN pipenv install --dev

COPY app ./

CMD pipenv run python ./manage.py migrate && pipenv run python ./manage.py runserver 0.0.0.0:8000