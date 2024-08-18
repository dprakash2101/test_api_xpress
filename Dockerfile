# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /action

# Copy the Python script and requirements file
COPY main.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point to the Python script
ENTRYPOINT ["python", "main.py"]
