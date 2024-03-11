import requests

class APIWrapper:
    def __init__(self, api_key=''):
        self.headers =api_key

    def api_get_request(self, url):
        response = requests.get(url,headers={f"Authorization": self.headers})
        if response.status_code == 200:
            return response
        else:
            print(f"Failed to get data: {response.status_code}, {response.text}")
            return None