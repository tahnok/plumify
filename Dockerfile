FROM python:3.5-alpine
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

RUN pip3 install pipenv

RUN mkdir /code
WORKDIR /code

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN set -ex && pipenv install --deploy --system

COPY . /code
RUN scripts/migrate
