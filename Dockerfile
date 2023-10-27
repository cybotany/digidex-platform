# Use an official Python runtime as the parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && \
    pip install gunicorn && \
    pip install -r requirements.txt && \
    echo 'export DJANGO_ENV="production"' >> ~/.bashrc && \
    echo 'export REGION_NAME="us-east-1"' >> ~/.bashrc

# Copy the content of the local src directory to the working directory
COPY . /app/

# Specify the command to run on container start
CMD ["gunicorn", "cybotany.wsgi:application", "--bind", "0.0.0.0:8000"]
