FROM python:stretch
LABEL maintainer="Kushal Hada <kushaldeveloper@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5000
ENTRYPOINT ["gunicorn","-w 2", "-b 0.0.0.0:5000", "app:app"]
