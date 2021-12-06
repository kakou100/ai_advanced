FROM python:3.7

RUN apt-get update

WORKDIR /usr/deploy

COPY . /usr/deploy/

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD gunicorn -w 3 -b :5000 -t 360 --reload wsgi:app
