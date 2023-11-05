FROM python:3.11.5

WORKDIR django_job_search_app

COPY requirements.txt /django_job_search_app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY .. .