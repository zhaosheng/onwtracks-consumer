FROM python:3.9-alpine3.13

RUN pip install paho-mqtt pytz

ADD src .
RUN chmod +x exporter.py

CMD ./exporter.py
