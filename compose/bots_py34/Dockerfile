FROM python:3.4

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app/src

COPY ./etc /requirements

RUN pip install --upgrade pip
RUN pip install -r /requirements/requirements.txt

COPY src/ /app/src
WORKDIR /app

CMD [ "python", "-u", "src/bots-webserver.py" ]
EXPOSE 9000
