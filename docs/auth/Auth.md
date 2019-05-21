# **ganb_auth**

All URIs are relative to *https://api.gmo-aozora.com/ganb/api/auth/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorization**]() | **POST** /authorization | 認可


### **authorization**
> GanbConnector(client_id, client_secret, auth_method, config)

認可

クライアントがユーザーの認証・認可を得るためのエンドポイント

### Example
```python
from ganb_personal_client.rest import ApiException as ApiPersonalException
from ganb_auth.authorization_api import GanbConnector, APITokenException, AuthMethod
import ganb_personal_client

CLIENT_ID = '<Your Client ID>'
CLIENT_SECRET = '<Your Client Secret>'
REDIRECT_URI = '<Your Registered Redirect URI>'
AUTH_METHOD = AuthMethod.BASIC  # AuthMethod.BASIC or POST

f = open('conf.json', 'r')
conf = json.load(f)

ganb = GanbConnector(CLIENT_ID,
                     CLIENT_SECRET,
                     AUTH_METHOD,
                     config=conf)
redirect_url = ganb.oauth_authorization(session_id, scope, REDIRECT_URI)
# If you want use openid => ganb.openid_authorization()

#Get OAuth token
try:
    token = ganb.get_oauth_token(REDIRECT_URI, code)
except APITokenException as e:
    print("Exception: ", e)

#Token refresh
try:
    new_token = ganb.refresh_session(token, e)
except APITokenException as e:
    print("Exception: ", e)
```

### Initialization parameters 
GanbConnector(client_id, client_secret, auth_method, config)

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **string**| client id |
 **client_secret** | **string**| client secret |
 **auth_method** | **AuthMethod**| BASIC or POST |
 **config** | **list**| "SALT"="","AUTH_BASE_URL"="","AUTH_PATH"="","TOKEN_PATH"="","JWT_ISSUER"="" |

### oauth_authorization(session_id, scope, redirect_uri)
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sessionID** | **string**| session id |
 **scope** | **string**| scope |
 **redirect_uri** | **string**| redirect uri |

### openid_authorization(session_id, scope, redirect_uri)
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **string**| session id |
 **scope** | **string**| scope |
 **redirect_uri** | **string**| redirect uri |

### get_oauth_token(redirect_uri, $code)
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_uri** | **string**| redirect uri |
 **code** | **string**| authorization code |

### get_openid_token($redirect_uri, $code)
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_uri** | **string**| redirect uri |
 **code** | **string**| authorization code |

### refresh_session($err, $token)
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **err** | **ApiException**| api error instance |
 **token** | **list**| token instance |