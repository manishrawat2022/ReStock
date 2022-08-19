FROM python:3.8

RUN pip install flask

WORKDIR /predictor

EXPOSE 8080

COPY . /predictor/

ENTRYPOINT [ "python", "server.py"]