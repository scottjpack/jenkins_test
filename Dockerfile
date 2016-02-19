FROM quadrode.com:5000/ubuntu:latest
RUN apt-get -q -y install python && apt-get -q -y install python-flask
ADD app.py /opt/app.py
RUN chmod +x /opt/app.py
