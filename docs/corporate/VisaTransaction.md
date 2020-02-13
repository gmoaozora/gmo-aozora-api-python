# VisaTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_date** | **str** | 利用日 半角文字 YYYY-MM-DD形式 | [optional]
**use_content** | **str** | 利用内容 全半角文字 | [optional]
**amount** | **str** | 利用金額 半角数字 マイナス含む 円貨金額 | [optional]
**local_currency_amount** | **str** | 現地通貨金額 半角数字 小数部最大6桁 マイナス含む 国内利用の場合は項目自体を設定しません | [optional]
**conversion_rate** | **str** | 円換算レート 半角数字 小数部最大6桁 マイナス含む 国内利用の場合は項目自体を設定しません | [optional]
**approval_number** | **str** | 承認番号 半角数字 | [optional]
**visa_status** | **str** |  ステータス 半角数字<br>1:確定・・・決済として完了している状態<br>2:未確定・・・加盟店からの情報によりお客様の口座から資金を引き落としていますが、決済としては完了していない状態<br>3:取消済・・・取消を行った状態 | [optional]
**currency_code** | **str** | 通貨コード 半角文字 ISO4217準拠した通貨コード 国内利用の場合は項目自体を設定しません | [optional]
**atm_comission** | **str** | ATM手数料 半角数字 小数部最大6桁 マイナス含む 現地通貨金額でのATM手数料<br>国内利用の場合または、ATM手数料自体が発生していない場合は項目自体を設定しません | [optional]
