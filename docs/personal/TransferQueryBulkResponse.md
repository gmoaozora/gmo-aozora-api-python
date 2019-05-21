# TransferQueryBulkResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **str** | 対象期間From 半角文字 リクエストしたときと同じ内容 対象期間（From）をYYYY-MM-DD形式で設定  | [optional] 
**date_to** | **str** | 対象期間To 半角文字 リクエストしたときと同じ内容 対象期間（To）をYYYY-MM-DD形式で設定  | [optional] 
**request_next_item_key** | **str** | リクエスト時次明細キー 半角数字 リクエストしたときと同じ内容 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**request_transfer_statuses** | [**list[RequestTransferStatus]**](RequestTransferStatus.md) | 振込一括照会対象ステータス 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**request_transfer_class** | **str** | 照会対象取得区分 半角数字 リクエストしたときと同じ内容 1：ALL、2：振込申請のみ、3：振込受付情報のみ 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**request_transfer_term** | **str** | 振込照会対象期間区分 半角数字 リクエストしたときと同じ内容 1：振込申請受付日　2：振込指定日 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**has_next** | **bool** | 次明細フラグ ・true&#x3D;次明細あり ・false&#x3D;次明細なし  | [optional] 
**next_item_key** | **str** | 次明細キー 半角数字 次明細フラグがfalseの場合は項目自体を設定しません  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


