# BulkTransferInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | 明細番号 半角数字 重複/0はエラー　1～9999とします  | [optional] 
**beneficiary_bank_code** | **str** | 被仕向金融機関番号 半角数字  | [optional] 
**beneficiary_bank_name** | **str** | 被仕向金融機関名カナ 半角文字 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**beneficiary_branch_code** | **str** | 被仕向支店番号 半角数字  | [optional] 
**beneficiary_branch_name** | **str** | 被仕向支店名カナ 半角文字 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**clearing_house_name** | **str** | 手形交換所番号 半角文字 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**account_type_code** | **str** | 科目コード（預金種別コード） 半角数字 1：普通、2：当座、4：貯蓄、9：その他  | [optional] 
**account_number** | **str** | 口座番号 半角数字 7桁未満の番号は右詰で、前ゼロで埋めること  | [optional] 
**beneficiary_name** | **str** | 受取人名 半角文字 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**transfer_amount** | **str** | 振込金額 半角数字 1以上9,999,999,999円以下　数値のみでカンマ、マイナス不可  | [optional] 
**new_code** | **str** | 新規コード 半角文字 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**edi_info** | **str** | EDI情報 半角文字 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**transfer_designated_type** | **str** | 振込指定区分 半角文字 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**identification** | **str** | 識別表示 半角文字 該当する情報が無い場合は項目自体を設定しません  | [optional] 
**transfer_detail_responses** | [**list[TransferDetailResponse]**](TransferDetailResponse.md) | 振込明細結果 振込明細結果のリスト 正常時のみ応答 該当する情報が無い場合は空のリストを返却  | [optional] 
**unable_detail_infos** | [**list[UnableDetailInfo]**](UnableDetailInfo.md) | 不能明細情報 不能明細情報のリスト 該当する情報が無い場合は項目自体を設定しません  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


