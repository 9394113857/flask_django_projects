# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file to the working directory
COPY requirements.txt /code/

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code to the working directory
COPY . /code/

# Expose the port that the Django development server will run on
EXPOSE 8000

# Set the command to run the Django development server
CMD python manage.py runserver 0.0.0.0:8000
