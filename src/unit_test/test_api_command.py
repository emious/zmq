import pytest
import requests

BASE_URL = "http://127.0.0.1:8100/api/v1/command"

def test_os_command():
    response = requests.post(
        BASE_URL,
        json={
            "command_type": "os",
            "command_name": "ping",
            "parameters": [
                "8.8.8.8",
                "-n",
                "2"
            ]
        }
    )
    assert response.status_code == 200
    assert 'Pinging' in response.json()['result'] ,  "Pinging not found in response"
    #assert response.json() == {"result": "expected_result_here"}

def test_compute_command():
    response = requests.post(
        BASE_URL,
        json={
            "command_type": "compute",
            "expression": "34*(1+5)"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"result": "204"}