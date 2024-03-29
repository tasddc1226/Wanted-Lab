FROM nikolaik/python-nodejs:python3.8-nodejs14

RUN mkdir /code

WORKDIR /code

ADD ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt
RUN pip install gunicorn

ADD . /code
RUN ["chmod", "+x", "start.sh"]
ENTRYPOINT ["sh", "./start.sh"]