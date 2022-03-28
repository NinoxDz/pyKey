FROM python:3.7

ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt &&\
    rm -rf ./requirements.txt

#ADD . /code
COPY src /app
RUN mkdir -p /app/results
WORKDIR /app

CMD ["python", "./run.py"]
