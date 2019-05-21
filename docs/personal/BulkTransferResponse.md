# BulkTransferResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | 口座ID 半角英数字 口座を識別するID  | [optional] 
**remitter_name** | **str** | 振込依頼人名 半角文字  | [optional] 
**transfer_designated_date** | **str** | 振込指定日 半角文字 YYYY-MM-DD形式  | [optional] 
**transfer_data_name** | **str** | 振込データ名 全半角文字 作成した総合振込のデータを区別するためのメモ  | [optional] 
**total_count** | **str** | 合計件数 半角数字  | [optional] 
**total_amount** | **str** | 合計金額 半角数字  | [optional] 
**bulk_transfer_infos** | [**list[BulkTransferInfo]**](BulkTransferInfo.md) | 総合振込明細情報 総合振込明細のリスト 明細情報取得フラグが「True：取得する」、かつ明細情報取得結果フラグが「True：取得可」のときのみ設定します それ以外は項目自体を設定しません  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


