# VaTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**va_id** | **str** | 振込入金口座ID 半角数字 振込入金口座を識別するID  | 
**transaction_date** | **str** | 取引日 半角文字 YYYY-MM-DD形式  | 
**value_date** | **str** | 起算日 半角文字 YYYY-MM-DD形式  | 
**va_branch_code** | **str** | 支店コード 半角数字  | 
**va_branch_name_kana** | **str** | 支店名カナ 半角文字  | 
**va_account_number** | **str** | 口座番号 半角数字  | 
**va_account_name_kana** | **str** | 口座名義カナ 半角文字  | 
**deposit_amount** | **str** | 入金金額 半角数字  | 
**remitter_name_kana** | **str** | 振込依頼人名カナ 半角文字  | 
**payment_bank_name** | **str** | 仕向金融機関名カナ 半角文字  | 
**payment_branch_name** | **str** | 仕向支店名カナ 半角文字  | 
**partner_name** | **str** | サービス企業名 全角文字 振込入金口座契約サービス企業名  | 
**remarks** | **str** | 摘要内容 全半角文字 該当データがない場合は項目自体を設定しません  | [optional] 
**item_key** | **str** | 明細キー 半角数字 口座ID毎に設定される明細キー（明細データtimestamp（μs）） | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


