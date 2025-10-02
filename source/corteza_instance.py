from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import os

class instance:
    """
    Class containing Corteza authentication session/token
    
    Basic usage:
    >>> corteza = corteza.corteza()
    >>> corteza_session = corteza.session
    """

    def __init__(self):
        self.__auth()

    def __auth(self):
        try:
            client_id=os.getenv('corteza_client_id')
            client_secret=os.getenv('corteza_client_secret')
            corteza_base_url=os.getenv('corteza_base_url')

            client = BackendApplicationClient(client_id=client_id)
            oauth = OAuth2Session(client=client)
            token = oauth.fetch_token(token_url= corteza_base_url + '/auth/oauth2/token', client_id=client_id, client_secret=client_secret, scope='api')
            self.session = OAuth2Session(client_id, token=token)
        except Exception as e:
            raise e
