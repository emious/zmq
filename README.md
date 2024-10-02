# FastAPI Project with ZMQ

## Description
This FastAPI project provides an API with two functionalities: executing OS commands and computing expressions.

### Compute Command
If the command type is `compute`, it takes an expression and evaluates it.

```json
{
  "command_type": "compute",
  "expression": "34*(1+5)"
}
```

### OS Command
If the command type is `os`, it executes a specified command on the server.

```json
{
  "command_type": "os",
  "command_name": "ping",
  "parameters": [
    "8.8.8.8",
    "-n", 
    "2"
  ]
}
```

## Getting Started

### Requirements
- Python 3.8+
- pip
- FastAPI
- (Optional) Docker
- requests
- pytest

### Installation

#### Using Docker
1. Build the Docker image:
   ```bash
   docker build -t zmq .
   ```
2. Run the Docker container:
   ```bash
   docker run zmq
   ```
3. Access the Swagger documentation at: [http://127.0.0.1:8100/docs](http://127.0.0.1:8100/docs)

#### Manual Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/emious/zmq.git
   cd <repository-directory>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python manage.py
   ```
4. Access the Swagger documentation at: [http://127.0.0.1:8100/docs](http://127.0.0.1:8100/docs)

## API Endpoints
URL: [http://127.0.0.1:8100/api/v1/command](http://127.0.0.1:8100/api/v1/command)

## Unit Test
To run tests:
```bash
cd repository-directory>/src/unit_test
pytest test_api_command.py
```
