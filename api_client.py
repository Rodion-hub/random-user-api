import requests


class APIClient:
    def __init__(self, api_url):
        self.api_url = api_url

    def get(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()

            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occerred: {err}")
            return None
        except Exception as err:
            print(f"An error occured: {err}")
            return None
