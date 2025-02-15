import requests
import logging

class RequestWrapper:
    def __init__(self):
        self.base_url = None

    def get(self, endpoint: str = None, params: dict = None, headers: dict = None):
        url = f"{endpoint}"
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

if __name__ == "__main__":
    api = RequestWrapper("https://jsonplaceholder.typicode.com")
    response = api.get("/todos/1")
    print(response)
