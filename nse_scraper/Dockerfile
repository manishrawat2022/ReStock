FROM python:3.8

COPY . /

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

CMD [ "python", "./main.py" ]

EXPOSE 5000
