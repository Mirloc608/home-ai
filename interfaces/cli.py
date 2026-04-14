import requests

def run_task(task: str):
    response = requests.post(
        "http://localhost:8000/task",
        json={"task": task},
    )
    print(response.json())
