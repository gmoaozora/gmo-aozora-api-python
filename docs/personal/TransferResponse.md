# TransferResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | 口座ID 半角数字 口座を識別するID 引き落とし元となる口座情報  | [optional] 
**remitter_name** | **str** | 振込依頼人名 半角文字  | [optional] 
**transfer_designated_date** | **str** | 振込指定日 半角文字 YYYY-MM-DD形式  | [optional] 
**transfer_infos** | [**list[TransferInfo]**](TransferInfo.md) | 振込情報 振込情報のリスト 該当する情報が無い場合は空のリストを返却  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


