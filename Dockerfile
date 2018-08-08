FROM python:3.6
ADD ./requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code
