#!/bin/sh

# Start ollama in the background
OLLAMA_HOST=0.0.0.0 ollama start &

# Wait for ollama to be ready
while ! ollama list; do
  echo "Waiting for ollama to start..."
  sleep 5
done

# Pull the llama3 model
ollama pull llama3

# Start the Python server
python server.py
