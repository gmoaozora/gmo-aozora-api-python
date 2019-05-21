# TransferError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | エラーコード 半角英数文字  | 
**error_message** | **str** | エラーメッセージ 全半角英数記号文字  | 
**error_details** | [**list[ErrorDetail]**](ErrorDetail.md) | エラー詳細情報 該当する情報が無い場合は空のリストを返却  | [optional] 
**transfer_error_details** | [**list[TransferErrorDetail]**](TransferErrorDetail.md) | 振込明細エラー情報 個別明細がエラーの場合のみ応答 該当する情報が無い場合は空のリストを返却  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


