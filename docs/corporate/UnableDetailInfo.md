# UnableDetailInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_detail_status** | **str** | 振込詳細ステータス 半角数字 1：手続済、2：手続不成立 手続中より前は該当する情報無しとみなし項目自体を設定しません  | [optional] 
**refund_status** | **str** | 組戻ステータス 半角数字 1：組戻手続中、2：組戻済、3：組戻不成立 組み戻しなし、および該当する情報が無い場合は項目自体を設定しません  | [optional] 
**is_repayment** | **bool** | 資金返却フラグ true&#x3D;あり 無し、および該当する情報が無い場合は項目自体を設定しません  | [optional] 
**repayment_date** | **str** | 資金返却日 半角文字 YYYY-MM-DD形式 総合振込のみ表示 該当する情報が無い場合は項目自体を設定しません  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


