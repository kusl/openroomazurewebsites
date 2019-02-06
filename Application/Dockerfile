FROM fedora:latest
LABEL maintainer="Kushal Hada <kushaldeveloper@gmail.com"
RUN dnf update -y
RUN dnf install -y python3 python3-pip python3-devel
RUN dnf groupinstall "Development Tools" "Development Libraries" -y
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
EXPOSE 5000
ENTRYPOINT ["gunicorn","-w 2", "-b 0.0.0.0:5000", "python_webapp_flask:app"]
