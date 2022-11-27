FROM python:3.10-alpine3.15

ENV PIP_ROOT_USER_ACTION=ignore

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN mkdir /app

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]