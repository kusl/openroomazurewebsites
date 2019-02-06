FROM debian:latest
LABEL maintainer="Kushal Hada <kushaldeveloper@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
EXPOSE 5000
ENTRYPOINT ["gunicorn","-w 2", "-b 0.0.0.0:5000", "app:app"]
