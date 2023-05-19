FROM python:3.11.3-alpine3.18

ADD . /root

WORKDIR /root

RUN pip install -r requirements.txt

ENTRYPOINT ["flask", "--app", "src", "run", "--host=0.0.0.0", "-p", "8888"]