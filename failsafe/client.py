import requests


class Client:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_root = 'https://www.bungie.net/Platform'
