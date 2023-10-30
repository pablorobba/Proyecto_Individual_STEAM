# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your application's code into the container
COPY . /app/

# Ejecuta la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
