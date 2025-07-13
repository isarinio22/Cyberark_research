# Use a lightweight Python base image for serving static files
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the HTML file into the container
# The HTML file is named 'index.html' based on your provided code
COPY index.html .

# Copy the Python application to serve the HTML
COPY main.py .

# Expose the port that the Flask app will listen on
EXPOSE 8080

# Run the Flask application
CMD ["python", "main.py"]
