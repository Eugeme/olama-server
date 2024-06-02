# Question and Answer Web App

This project is a simple web-based application that allows users to ask questions and get responses using the `ollama` chat model. The server is implemented in Python using the `http.server` module, and the front-end is built with HTML, CSS, and JavaScript.

## Features

- A web interface where users can submit questions.
- The server processes the questions and returns responses using the `ollama` chat model.
- The web page has a user-friendly design with a grey background and a responsive design.

## Prerequisites

- Python 3.x
- `ollama` library (Ensure it's installed and properly configured)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Eugeme/olama-server.git
    cd olama-server
    ```

2. **Install the required Python packages**:
    ```bash
    pip install ollama
    ```

3. **Create the necessary files**:
    - `server.py` (The main Python server file)
    - `index.html` (The front-end HTML file)

## Running the Server

1. **Run the server**:
    ```bash
    python server.py
    ```

2. **Open your browser** and go to `http://127.0.0.1:9999` to see the web interface.

## Usage

- Open your web browser and navigate to `http://127.0.0.1:9999`.
- Enter your question in the input box and click "Submit".
- The server will process your question using the `ollama` chat model and display the response on the page.

## License

This project is licensed under the MIT License.