from failsafe.session import Session
from failsafe.services.manifest import ManifestApi


class Client:
    def __init__(self, api_key: str, manifest_api=ManifestApi):
        self.session = Session(api_key=api_key)
        self.api_root = 'https://www.bungie.net/Platform'
        self.manifest = manifest_api(session=self.session)
