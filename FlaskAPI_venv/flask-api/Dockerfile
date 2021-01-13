FROM python:3.9-slim-buster

MAINTAINER "Eran Hadad"

#copy requirements first
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "run_app.py" ]