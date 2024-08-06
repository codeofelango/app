# FROM python:3.8-slim


# WORKDIR /app


# COPY . ./


# RUN pip install flask gunicorn  google-cloud-bigquery

# # ENV PORT=8080


# # CMD ["python", "run.py"]

# CMD gunicorn --bind :$PORT app:app



# Use an official Python runtime as a parent image
FROM python:3.9-slim
# Set the working directory in the container
WORKDIR /app
# Copy the current directory contents into the container at /usr/src/app
COPY . .
# Install any needed dependencies specified in requirements.txt
RUN pip install flask gunicorn  google-cloud-bigquery

# Make port 5000 available to the world outside this container
# EXPOSE 5000
# Define environment variable
# ENV FLASK_APP=run.py
# Run app.py when the container launches
# CMD ["gunicorn", "-b", ":5000", "app:run"]


CMD gunicorn --bind :$PORT app:app

