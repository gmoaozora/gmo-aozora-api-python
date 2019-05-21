# TransferCancelRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | 口座ID 半角英数字 口座を識別するID  | 
**cancel_target_key_class** | **str** | 取消対象キー区分 半角英数値 取消対象の取引の内容について指定します 1:振込申請取消　2:振込受付取消　3:総合振込申請取消　4:総合振込受付取消 取消対象キー区分と、取消対象の振込申請番号の状態がマッチしない場合は、「400 Bad Request」を返却  | 
**apply_no** | **str** | 受付番号（振込申請番号） 半角数字 取り消し対象の番号を設定  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


