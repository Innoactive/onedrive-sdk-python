from auth_provider_base import AuthProviderBase
from .session import Session
from .options import *

class SocialAuthProvider(AuthProviderBase):

    def __init__(self, access_token, http_provider=None, client_id=None, scopes=None):
        self._session = Session(None, 0, '', access_token, None, None, None)

    @property
    def client_id(self):
        raise NotImplementedError

    @client_id.setter
    def client_id(self, value):
        raise NotImplementedError

    @property
    def scopes(self):
        raise NotImplementedError

    @scopes.setter
    def scopes(self, value):
        raise NotImplementedError

    @property
    def access_token(self):
        return self._session.acces_token

    @access_token.setter
    def access_token(self, value):
        self._session.access_token = value

    def get_auth_url(self, auth_server_url, redirect_uri):
        raise NotImplementedError

    def authenticate(self, code, auth_server_url, redirect_uri, client_secret, resource):
        raise NotImplementedError

    def authenticate_request(self, request):
        request.append_option(
            HeaderOption("Authorization",
                         "bearer {}".format(self._session.access_token)))

    def refresh_token(self):
        raise NotImplementedError