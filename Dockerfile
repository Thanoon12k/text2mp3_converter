
FROM python:3.8-slim-buster
# Added the EXPOSE command to specify the port that will be used
EXPOSE 8000
ENV PYTHONBUFFERED=1 
WORKDIR /djangofolder
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
