# GMO Aozora Net Bank Open Api Python SDK

## About

GMOあおぞらネット銀行について

https://gmo-aozora.com/

GMOあおぞらネット銀行 API開発者ポータルについて

https://api.gmo-aozora.com/ganb/developer/

## Version 
1.0.0

## Requirements

Python 3.5+

## Installation & Usage
### pip install

```sh
pip install git-https://github.com/gmoaozora/gmo-aozora-api-python.git
```

Then import the package
```python
import ganb_auth
import ganb_personal_client
import ganb_corporate_client
```

### Setuptools

```sh
python setup.py install --user
```

Then import the package
```python
import ganb_auth
import ganb_personal_client
import ganb_corporate_client
```
## Getting start

### Enviroment

Add the configuration below into your config file

* stg

    conf.json
    ```json
    {
        "AUTH_BASE_URL": "https://stg-api.gmo-aozora.com/ganb/api/auth/v1",
        "JWT_ISSUER": "https://stg-api.gmo-aozora.com/",
        "AUTH_PATH": "/authorization",
        "TOKEN_PATH": "/token",
        "SALT": "PleaseDefineYourself"
    }
    ```
    [configuration.py - Personal ](./ganb_personal_client/configuration.py) 
    ```python
        self.host = "https://stg-api.gmo-aozora.com/ganb/api/personal/v1"
    ```
    [configuration.py - Corporate ](./ganb_corporate_client/configuration.py) 
    ```python
        self.host = "https://stg-api.gmo-aozora.com/ganb/api/corporation/v1"
    ```
    [configuration.py - Webhook ](./ganb_webhook_client/configuration.py) 
    ```python
        self.host = "https://stg-api.gmo-aozora.com/ganb/api/webhook/v1"
    ```

* prod

    conf.json
    ```json
    {
        "AUTH_BASE_URL": "https://api.gmo-aozora.com/ganb/api/auth/v1",
        "JWT_ISSUER": "https://api.gmo-aozora.com/",
        "AUTH_PATH": "/authorization",
        "TOKEN_PATH": "/token",
        "SALT": "PleaseDefineYourself"
    }
    ```
    [configuration.py - Personal ](./ganb_personal_client/configuration.py) 
    ```python
        self.host = "https://api.gmo-aozora.com/ganb/api/personal/v1"
    ```
    [configuration.py - Corporate ](./ganb_corporate_client/configuration.py) 
    ```python
        self.host = "https://api.gmo-aozora.com/ganb/api/corporation/v1"
    ```
    [configuration.py - Webhook ](./ganb_webhook_client/configuration.py) 
    ```python
        self.host = "https://api.gmo-aozora.com/ganb/api/webhook/v1"
    ```

## API Documents
* [**Auth**](./docs/auth/)
* [**Personal**](./docs/personal/)
* [**Corporate**](./docs/corporate/)
* [**Webhook**](./docs/webhook)


## Author

GMO Aozora Net Bank, Ltd. (open-api@gmo-aozora.com)

## license

[MIT](https://github.com/gmoaozora/gmo-aozora-api-python/blob/master/LICENSE)
