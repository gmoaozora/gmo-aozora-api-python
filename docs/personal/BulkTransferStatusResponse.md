# BulkTransferStatusResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptance_key_class** | **str** | 照会対象キー区分 半角数字 リクエストしたときと同じ内容 照会対象のキー 1：振込申請照会対象指定、2：振込一括照会対象指定  | 
**detail_info_necessity** | **bool** | 明細情報取得フラグ 総合振込明細情報の取得要否 リクエストしたときと同じ内容 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**bulktransfer_item_key** | **str** | 総合振込明細情報取得対象キー 半角数字 リクエストしたときと同じ内容 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**base_date** | **str** | 基準日 半角文字 総合振込照会明細情報を照会した基準日を示します YYYY-MM-DD形式  | 
**base_time** | **str** | 基準時刻 半角文字 総合振込照会明細情報を照会した基準時刻を示します HH:MM:SS+09:00形式  | 
**count** | **str** | 明細取得件数 半角数字 振込明細の件数  | 
**detail_info_result** | **bool** | 明細情報取得結果フラグ 総合振込明細情報の取得結果 True：取得可、False:取得不可 明細情報取得フラグが「True：取得する」のときに、明細情報が取得できたかを設定します 総合振込の依頼完了直後は「False:取得不可」となります 総合振込の依頼完了後１０分程度すると「True：取得可」となります 「False:取得不可」の場合、総合振込明細情報は項目自体が設定されません 明細情報取得フラグが「True：取得する」の場合以外は項目自体を設定しません  | [optional] 
**transfer_query_bulk_responses** | [**list[TransferQueryBulkResponse]**](TransferQueryBulkResponse.md) | 振込一括照会対象指定レスポンス 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**bulk_transfer_details** | [**list[BulkTransferDetail]**](BulkTransferDetail.md) | 総合振込照会明細情報 振込照会明細情報のリスト 該当する情報が無い場合は空のリストを返却  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


