FROM python:3.4

ENV PYTHONUNBUFFERED 1

COPY ./etc /requirements

RUN pip install --upgrade pip
RUN pip install -r /requirements/requirements.txt

COPY src/ /bots
COPY scripts/ /bots
WORKDIR /bots

CMD [ "python", "-u", "bots-webserver.py" ]
EXPOSE 9000
