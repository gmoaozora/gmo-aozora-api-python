# AccountsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **str** | 基準日 半角文字 一覧照会の基準日を示します YYYY-MM-DD形式  | 
**base_time** | **str** | 基準時刻 半角文字 一覧照会の基準時刻を示します HH:MM:SS+09:00形式  | 
**accounts** | [**list[Account]**](Account.md) | 口座情報リスト  | 
**sp_accounts** | [**list[SpAccount]**](SpAccount.md) | つかいわけ口座情報リスト 該当する情報が無い場合は、項目自体を設定しません  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


