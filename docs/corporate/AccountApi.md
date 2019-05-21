# ganb_corporate_client.AccountApi

All URIs are relative to *https://stg-api.gmo-aozora.com/ganb/api/corporation/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_deposit_transactions_using_get**](AccountApi.md#accounts_deposit_transactions_using_get) | **GET** /accounts/deposit-transactions | 振込入金明細照会
[**accounts_using_get**](AccountApi.md#accounts_using_get) | **GET** /accounts | 口座一覧照会
[**balances_using_get**](AccountApi.md#balances_using_get) | **GET** /accounts/balances | 残高照会
[**transactions_using_get**](AccountApi.md#transactions_using_get) | **GET** /accounts/transactions | 入出金明細照会


# **accounts_deposit_transactions_using_get**
> DepositTransactionsResponse accounts_deposit_transactions_using_get(account_id, x_access_token, date_from=date_from, date_to=date_to, next_item_key=next_item_key)

振込入金明細照会

<p>指定した円普通預金口座の振込入金明細情報を照会します</p> <h4 style='margin-top:30px; border-left: solid 4px #1B2F48; padding: 0.1em 0.5em; color:#1B2F48;'>詳細説明</h4> <div style='margin:10px;'>   <p style='font-weight:bold; color:#616161;'>対象科目</p>   <p style='padding-left:20px;'>円普通預金口座</p> </div> <div style='margin:10px;'>   <p style='font-weight:bold; color:#616161;'>取得上限件数</p>   <p style='padding-left:20px;'>500件</p>   <p style='padding-left:20px;'>取得できる明細数が500に満たないときは取得できる明細のみを返却します</p>   <p style='padding-left:20px;'>取得できる明細が存在しない場合は「200：OK」とし明細を返却しません</p> </div> <div style='margin:10px;'>   <p style='font-weight:bold; color:#616161;'>ページング</p>   <p style='padding-left:20px;'>2ページ目以降を照会する際は、初回と同じリクエスト内容に、初回レスポンスの次明細キーを追加してリクエストしてください</p> </div> <div style='margin:10px;'>   <p style='font-weight:bold; color:#616161;'>ソート順</p>   <p style='padding-left:20px;'>取引の昇順</p> </div> <div style='width:600px; margin:10px;'>   <p style='font-weight:bold; color:#616161;'>対象期間</p>   <div style='display:table; margin-left:20px; background-color:#29659b;'>     <div style='display:table-cell; width:160px; padding:9px; border:1px solid #fff; color:#fff;'>日本語名</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; text-align:center; font-size:120%; color:#fff;'>&#9312;</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; text-align:center; font-size:120%; color:#fff;'>&#9313;</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; text-align:center; font-size:120%; color:#fff;'>&#9314;</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; text-align:center; font-size:120%; color:#fff;'>&#9315;</div>   </div>   <div style='display:table; margin-left:20px;'>     <div style='display:table-cell; width:160px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>対象期間From</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>×</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>○</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>×</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>○</div>   </div>   <div style='display:table; margin-left:20px;'>     <div style='display:table-cell; width:160px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>対象期間To</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>×</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>×</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>○</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>○</div>   </div> </div> <div style='margin:10px;'>   <ul>     <li style='list-style-type:none;'>&#9312;の場合　当日分の振込入金明細を返却</li>     <li style='list-style-type:none;'>&#9313;の場合　対象期間From　～　当日までの振込入金明細を返却</li>     <li style='list-style-type:none;'>&#9314;の場合　取引初回　～　対象期間Toまでの振込入金明細を返却</li>     <li style='list-style-type:none;'>&#9315;の場合　対象期間From　～　対象期間Toまでの振込入金明細を返却</li>   </ul> </div> <div style='margin-bottom:40px;' /> 

### Example
```python
from __future__ import print_function
import time
import ganb_corporate_client
from ganb_corporate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ganb_corporate_client.AccountApi()
account_id = '\"101011234567\"' # str | 口座ID 半角数字 口座を識別するID  minLength: 12 maxLength: 29 
x_access_token = 'x_access_token_example' # str | アクセストークン  minLength: 1 maxLength: 128 
date_from = '\"2018-07-30\"' # str | 対象期間From 半角文字 YYYY-MM-DD形式  minLength: 10 maxLength: 10  (optional)
date_to = '\"2018-08-10\"' # str | 対象期間To 半角文字 YYYY-MM-DD形式  対象期間Fromと対象期間Toを指定する場合は、対象期間From≦対象期間Toとし、それ以外は「400 Bad Request」を返却  minLength: 10 maxLength: 10  (optional)
next_item_key = '\"20181012090520123456\"' # str | 次明細キー 半角数字 初回要求時は未設定 初回応答で次明細フラグが「true」の場合、返却された同項目を2回目以降に設定  minLength: 1 maxLength: 24  (optional)

try:
    # 振込入金明細照会
    api_response = api_instance.accounts_deposit_transactions_using_get(account_id, x_access_token, date_from=date_from, date_to=date_to, next_item_key=next_item_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->accounts_deposit_transactions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| 口座ID 半角数字 口座を識別するID  minLength: 12 maxLength: 29  | 
 **x_access_token** | **str**| アクセストークン  minLength: 1 maxLength: 128  | 
 **date_from** | **str**| 対象期間From 半角文字 YYYY-MM-DD形式  minLength: 10 maxLength: 10  | [optional] 
 **date_to** | **str**| 対象期間To 半角文字 YYYY-MM-DD形式  対象期間Fromと対象期間Toを指定する場合は、対象期間From≦対象期間Toとし、それ以外は「400 Bad Request」を返却  minLength: 10 maxLength: 10  | [optional] 
 **next_item_key** | **str**| 次明細キー 半角数字 初回要求時は未設定 初回応答で次明細フラグが「true」の場合、返却された同項目を2回目以降に設定  minLength: 1 maxLength: 24  | [optional] 

### Return type

[**DepositTransactionsResponse**](DepositTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_using_get**
> AccountsResponse accounts_using_get(x_access_token)

口座一覧照会

保有する全ての口座情報一覧を照会します

### Example
```python
from __future__ import print_function
import time
import ganb_corporate_client
from ganb_corporate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ganb_corporate_client.AccountApi()
x_access_token = 'x_access_token_example' # str | アクセストークン  minLength: 1 maxLength: 128 

try:
    # 口座一覧照会
    api_response = api_instance.accounts_using_get(x_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->accounts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| アクセストークン  minLength: 1 maxLength: 128  | 

### Return type

[**AccountsResponse**](AccountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balances_using_get**
> BalancesResponse balances_using_get(x_access_token, account_id=account_id)

残高照会

保有する口座の残高情報を照会します 口座IDを指定した場合、該当する口座の残高情報を照会します 口座IDを指定しない場合、保有する口座全ての残高情報を照会します 

### Example
```python
from __future__ import print_function
import time
import ganb_corporate_client
from ganb_corporate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ganb_corporate_client.AccountApi()
x_access_token = 'x_access_token_example' # str | アクセストークン  minLength: 1 maxLength: 128 
account_id = '\"101011234567\"' # str | 口座ID 口座を識別するID  minLength: 12 maxLength: 29  (optional)

try:
    # 残高照会
    api_response = api_instance.balances_using_get(x_access_token, account_id=account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->balances_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| アクセストークン  minLength: 1 maxLength: 128  | 
 **account_id** | **str**| 口座ID 口座を識別するID  minLength: 12 maxLength: 29  | [optional] 

### Return type

[**BalancesResponse**](BalancesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_using_get**
> TransactionsResponse transactions_using_get(account_id, x_access_token, date_from=date_from, date_to=date_to, next_item_key=next_item_key)

入出金明細照会

<p>指定した円普通預金口座の入出金明細情報を照会します</p> <h4 style='margin-top:30px; border-left: solid 4px #1B2F48; padding: 0.1em 0.5em; color:#1B2F48;'>詳細説明</h4> <div style='margin:10px;'>   <p style='font-weight:bold; color:#616161;'>対象科目</p>   <p style='padding-left:20px;'>円普通預金口座</p> </div> <div style='margin:10px;'>   <p style='font-weight:bold; color:#616161;'>取得上限件数</p>   <p style='padding-left:20px;'>500件</p>   <p style='padding-left:20px;'>取得できる明細数が500に満たないときは取得できる明細のみを返却します</p>   <p style='padding-left:20px;'>取得できる明細が存在しない場合は「200：OK」とし明細を返却しません</p> </div> <div style='margin:10px;'>   <p style='font-weight:bold; color:#616161;'>ページング</p>   <p style='padding-left:20px;'>2ページ目以降を照会する際は、初回と同じリクエスト内容に、初回レスポンスの次明細キーを追加してリクエストしてください</p> </div> <div style='margin:10px;'>   <p style='font-weight:bold; color:#616161;'>ソート順</p>   <p style='padding-left:20px;'>取引の昇順</p> </div> <div style='width:600px; margin:10px;'>   <p style='font-weight:bold; color:#616161;'>対象期間</p>   <div style='display:table; margin-left:20px; background-color:#29659b;'>     <div style='display:table-cell; width:160px; padding:9px; border:1px solid #fff; color:#fff;'>日本語名</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; text-align:center; font-size:120%; color:#fff;'>&#9312;</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; text-align:center; font-size:120%; color:#fff;'>&#9313;</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; text-align:center; font-size:120%; color:#fff;'>&#9314;</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; text-align:center; font-size:120%; color:#fff;'>&#9315;</div>   </div>   <div style='display:table; margin-left:20px;'>     <div style='display:table-cell; width:160px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>対象期間From</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>×</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>○</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>×</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>○</div>   </div>   <div style='display:table; margin-left:20px;'>     <div style='display:table-cell; width:160px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>対象期間To</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>×</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>×</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>○</div>     <div style='display:table-cell; width:80px; padding:9px; border:1px solid #fff; background-color:#f8f8f8; font-size:120%; text-align:center;'>○</div>   </div> </div> <div style='margin:10px;'>   <ul>     <li style='list-style-type:none;'>&#9312;の場合　当日分の入出金明細を返却</li>     <li style='list-style-type:none;'>&#9313;の場合　対象期間From　～　当日までの入出金明細を返却</li>     <li style='list-style-type:none;'>&#9314;の場合　取引初回　～　対象期間Toまでの入出金明細を返却</li>     <li style='list-style-type:none;'>&#9315;の場合　対象期間From　～　対象期間Toまでの入出金明細を返却</li>   </ul> </div> <div style='margin-bottom:40px;' /> 

### Example
```python
from __future__ import print_function
import time
import ganb_corporate_client
from ganb_corporate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ganb_corporate_client.AccountApi()
account_id = '\"101011234567\"' # str | 口座ID 半角英数字 口座を識別するID 科目コードが以下の場合のみ受け付けます ・01=普通預金（有利息） ・02=普通預金（決済用）  minLength: 12 maxLength: 29 
x_access_token = 'x_access_token_example' # str | アクセストークン  minLength: 1 maxLength: 128            
date_from = '\"2018-07-30\"' # str | 対象期間From 半角文字 YYYY-MM-DD形式  minLength: 10 maxLength: 10  (optional)
date_to = '\"2018-08-10\"' # str | 対象期間To 半角文字 YYYY-MM-DD形式 対象期間Fromと対象期間Toを指定する場合は、対象期間From≦対象期間Toとし、それ以外は「400 Bad Request」を返却  minLength: 10 maxLength: 10  (optional)
next_item_key = '\"20181012090520112541\"' # str | 次明細キー 半角数字 初回要求時は未設定 初回応答で次明細キーが「true」の場合、返却された同項目を2回目以降に設定  minLength: 1 maxLength: 24  (optional)

try:
    # 入出金明細照会
    api_response = api_instance.transactions_using_get(account_id, x_access_token, date_from=date_from, date_to=date_to, next_item_key=next_item_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->transactions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| 口座ID 半角英数字 口座を識別するID 科目コードが以下の場合のみ受け付けます ・01&#x3D;普通預金（有利息） ・02&#x3D;普通預金（決済用）  minLength: 12 maxLength: 29  | 
 **x_access_token** | **str**| アクセストークン  minLength: 1 maxLength: 128             | 
 **date_from** | **str**| 対象期間From 半角文字 YYYY-MM-DD形式  minLength: 10 maxLength: 10  | [optional] 
 **date_to** | **str**| 対象期間To 半角文字 YYYY-MM-DD形式 対象期間Fromと対象期間Toを指定する場合は、対象期間From≦対象期間Toとし、それ以外は「400 Bad Request」を返却  minLength: 10 maxLength: 10  | [optional] 
 **next_item_key** | **str**| 次明細キー 半角数字 初回要求時は未設定 初回応答で次明細キーが「true」の場合、返却された同項目を2回目以降に設定  minLength: 1 maxLength: 24  | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

