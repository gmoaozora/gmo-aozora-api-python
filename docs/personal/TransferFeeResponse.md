# TransferFeeResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | 口座ID 半角英数字 口座を識別するID  | 
**base_date** | **str** | 基準日 振込の手数料を照会した基準日を示します YYYY-MM-DD形式  | 
**base_time** | **str** | 基準時刻 振込の手数料を照会した基準時刻を示します HH:MM:SS+09:00形式  | 
**total_fee** | **str** | 合計振込手数料 半角数字 手数料の合計額を表示  | 
**transfer_fee_details** | [**list[TransferFeeDetail]**](TransferFeeDetail.md) | 振込手数料明細情報 個別明細を設定  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


