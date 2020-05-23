FROM ubuntu
RUN apt-get update
RUN apt-get install python
COPY . /opt/app
CMD[python insert-scripy.py]