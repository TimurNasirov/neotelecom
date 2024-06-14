FROM python:3.6

COPY core /core

RUN set -x \
    && pip install -r core/requirements.txt

WORKDIR /core
