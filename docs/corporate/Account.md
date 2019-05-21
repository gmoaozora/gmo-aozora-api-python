# Account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | 口座ID 半角英数字 口座を識別するID  | 
**branch_code** | **str** | 支店コード 半角数字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01&#x3D;普通預金（有利息） ・02&#x3D;普通預金（決済用）  | [optional] 
**branch_name** | **str** | 支店名 全角文字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01&#x3D;普通預金（有利息） ・02&#x3D;普通預金（決済用）  | [optional] 
**account_type_code** | **str** | 科目コード 半角数字 ・01&#x3D;普通預金（有利息） ・02&#x3D;普通預金（決済用） ・11&#x3D;円定期預金 ・51&#x3D;外貨普通預金 ・81&#x3D;証券コネクト口座  | 
**account_type_name** | **str** | 科目名 全角文字 科目コードの名称  | 
**account_number** | **str** | 口座番号 半角数字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01&#x3D;普通預金（有利息） ・02&#x3D;普通預金（決済用）  | [optional] 
**primary_account_code** | **str** | 代表口座コード 半角数字 ・1&#x3D;代表口座 ・2&#x3D;追加口座 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01&#x3D;普通預金（有利息） ・02&#x3D;普通預金（決済用）  | [optional] 
**primary_account_code_name** | **str** | 代表口座コード名 全角文字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01&#x3D;普通預金（有利息） ・02&#x3D;普通預金（決済用）  | [optional] 
**account_name** | **str** | 口座名義 全角文字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01&#x3D;普通預金（有利息） ・02&#x3D;普通預金（決済用）  | [optional] 
**account_name_kana** | **str** | 口座名義カナ 半角文字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01&#x3D;普通預金（有利息） ・02&#x3D;普通預金（決済用）  | [optional] 
**currency_code** | **str** | 通貨コード 半角文字 ISO4217に準拠した通貨コード  | 
**currency_name** | **str** | 通貨名 全角文字 ISO4217に準拠した通貨コードの当行での名称  | 
**transfer_limit_amount** | **str** | 振込限度額 半角数字 科目コードが以下の場合のみ設定されます 該当しない場合は項目自体を設定しません ・01&#x3D;普通預金（有利息） ・02&#x3D;普通預金（決済用）  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


