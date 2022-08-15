FROM python:3.8

ADD colab-requirements.txt /

RUN pip install -r /requirements.txt

RUN pip install requests_html

RUN pip install "pymongo[srv]"

ADD moneycontrol.py /

ENV PYTHONUNBUFFERED=1

CMD [ "python", "./iris-classifier.py" ]