# Pull the base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /TXTSPEAK

# Set work directory
WORKDIR /TXTSPEAK

# Install dependencies
COPY requirements.txt /TXTSPEAK/
RUN pip install -r requirements.txt

# Copy project
COPY . /TXTSPEAK/