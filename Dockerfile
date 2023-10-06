# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
&& apt-get install -y --no-install-recommends gcc libpq-dev \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
&& pip install -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/
