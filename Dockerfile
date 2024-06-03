# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install necessary dependencies for ollama
RUN apt-get update && apt-get install -y \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install ollama using the provided command
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Make port 9999 available to the world outside this container
EXPOSE 9999

# Define environment variable
ENV HOST=0.0.0.0
ENV PORT=9999

# Copy the startup script
COPY start.sh .

# Ensure the startup script is executable
RUN chmod +x start.sh

# Run the startup script
CMD ["./start.sh"]