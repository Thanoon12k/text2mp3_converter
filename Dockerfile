
FROM python:3.8-slim-buster
# Added the EXPOSE command to specify the port that will be used
EXPOSE 8000
ENV PYTHONBUFFERED=1 
WORKDIR /djangofolder
# Changed the COPY command to copy the requirements.txt file to the /djangofolder directory
COPY requirements.txt /djangofolder
# Added the RUN command to install the required packages from requirements.txt
RUN pip install -r requirements.txt
