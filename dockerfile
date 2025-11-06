# Use an official lightweight Python base image
FROM python:3.10-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy all files from your local project folder to /app in the container
COPY . /app

# Update and install system dependencies if needed (e.g., AWS CLI, git)
RUN apt-get update -y && apt-get install -y awscli git

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (if your FastAPI/Flask app uses one)
EXPOSE 8080

# Command to run your ML pipeline or FastAPI app
# You can change main.py to the
