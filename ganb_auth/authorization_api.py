import urllib
from urllib import parse, request, error
import json
import uuid
import hashlib
import base64
import jwt
import os

from enum import Enum


class APITokenException(Exception):
    pass


class AuthMethod(Enum):
    BASIC = "basic"
    POST = "post"


class GanbConnector:

    def __init__(self, client_id, client_secret, auth_method, config=None, nonce=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_method = auth_method
        self.nonce = nonce
        self.config = config

    def oauth_authorization(self, session_id, scope, redirect_uri):
        state = get_state(session_id, self.config['SALT'])

        param = parse.urlencode({"response_type": "code",
                                 "scope": scope,
                                 "client_id": self.client_id,
                                 "state": state,
                                 "redirect_uri": redirect_uri
                                })

        return self.config['AUTH_BASE_URL']+self.config['AUTH_PATH']+'?'+param

    def get_oauth_token(self, redirect_uri, code):
        param = {}
        param['code'] = code
        param['redirect_uri'] = redirect_uri
        param['grant_type'] = 'authorization_code'

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        token_url = self.config['AUTH_BASE_URL']+self.config['TOKEN_PATH']

        if (self.auth_method == AuthMethod.BASIC):
            headers['Authorization'] = authorization_header(self.client_id,
                                                            self.client_secret)
        else:
            param['client_id'] = self.client_id
            param['client_secret'] = self.client_secret

        # set query param end request
        data = parse.urlencode(param).encode('utf-8')
        req = request.Request(token_url, data, headers)

        try:
            response = request.urlopen(req)
            token = json.loads(response.read().decode('utf-8'))
            if 'access_token' in token and 'refresh_token' in token:
                return token
            else:
                raise APITokenException("token format error")
        except error.HTTPError as e:
            raise APITokenException(e.read().decode('utf-8'))
        except ValueError as e:
            raise APITokenException("token value error")

    def openid_authorization(self, session_id, scope, redirect_uri):
        state = get_state(session_id, self.config['SALT'])

        # create and save nonce each request
        nonce = str(uuid.uuid4())
        store_nonce(nonce)

        param = parse.urlencode({"response_type": "code",
                                 "scope": scope,
                                 "client_id": self.client_id,
                                 "redirect_uri": redirect_uri,
                                 "nonce": load_nonce(),
                                 "state": state})

        return self.config['AUTH_BASE_URL']+self.config['AUTH_PATH']+'?'+param

    def get_openid_token(self, redirect_uri, code):
        token_url = self.config['AUTH_BASE_URL']+self.config['TOKEN_PATH']
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        param = {}
        param['grant_type'] = 'authorization_code'
        param['code'] = code
        param['redirect_uri'] = redirect_uri

        if (self.auth_method == AuthMethod.BASIC):
            headers['Authorization'] = authorization_header(self.client_id,
                                                            self.client_secret)
        else:
            param['client_id'] = self.client_id
            param['client_secret'] = self.client_secret

        data = parse.urlencode(param).encode("utf-8")
        req = request.Request(token_url, data, headers)

        try:
            response = request.urlopen(req)
            token = json.loads(response.read().decode('utf-8'))
            if 'access_token' in token and \
               'refresh_token' in token and \
               'id_token' in token:
                if self.is_valid_token(token['id_token'], load_nonce()):
                    return token
                else:
                    raise APITokenException("invalid token error")
            else:
                raise APITokenException("token format error")
        except error.HTTPError as e:
            raise APITokenException(e.read().decode('utf-8'))
        except ValueError as e:
            raise APITokenException("token value error")

    def refresh_tokens(self, refresh_token):
        token_url = self.config['AUTH_BASE_URL']+self.config['TOKEN_PATH']
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        param = {}
        param['grant_type'] = 'refresh_token'
        param['refresh_token'] = refresh_token
        if (self.auth_method == AuthMethod.BASIC):
            headers['Authorization'] = authorization_header(self.client_id,
                                                            self.client_secret)
        else:
            param['client_id'] = self.client_id
            param['client_secret'] = self.client_secret

        data = parse.urlencode(param).encode("utf-8")
        req = request.Request(token_url, data, headers)

        try:
            response = request.urlopen(req)
            token = json.loads(response.read().decode('utf-8'))
            if 'access_token' in token and 'refresh_token' in token:
                return token
            else:
                raise APITokenException("token format error")
        except error.HTTPError as e:
            raise APITokenException(e.read().decode('utf-8'))
        except ValueError as e:
            raise APITokenException("token value error")

    def is_valid_token(self, id_token, nonce):
        payload = jwt.decode(id_token,
                             self.client_secret,
                             issuer=self.config['JWT_ISSUER'],
                             audience=self.client_id,
                             algorithms=['HS256'])
        if payload['nonce'] == nonce:
            return True
        return False


def get_state(session_id, salt):
    return hashlib.sha256((session_id+salt).encode('utf-8')).hexdigest()


def authorization_header(client_id, client_secret):
    base64_encoded_client = base64.b64encode((client_id+':'+client_secret)
                                             .encode('utf-8'))
    return 'Basic '+base64_encoded_client.decode('utf-8')


def store_nonce(nonce):
    # implement nonce store solution ex) file, db
    return None


def load_nonce():
    # implement nonce load solution
    return "Your saved nonce"


def get_config():
    f = open(os.path.dirname(__file__)+'/conf.json', 'r')
    return json.load(f)
