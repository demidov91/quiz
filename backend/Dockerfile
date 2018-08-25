FROM python:3.7-stretch

ADD . /backend
WORKDIR /backend
RUN pip install -r requirements.txt

CMD ./start_server.sh
