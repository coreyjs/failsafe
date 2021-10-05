from failsafe.services import BaseService, HttpMethod
from failsafe.session import Session


class ManifestApi(BaseService):
    def __init__(self, session: Session):
        super(ManifestApi, self).__init__(session=session)
        self.name = 'manifest'

    def get(self):
        url = self.base_api_root + 'Destiny2/Manifest'
        self.call(method=HttpMethod.GET, url=url)

    def get(self, entity_type: str, hash: str):
        self.call()