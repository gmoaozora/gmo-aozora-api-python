# coding: utf-8

"""
    GMO Aozora Net Bank Open API

    <p>オープンAPI仕様書（PDF版）は下記リンクをご参照ください</p> <div>   <div style='display:inline-block;'><a style='text-decoration:none; font-weight:bold; color:#00b8d4;' href='https://gmo-aozora.com/business/service/api-specification.html' target='_blank'>オープンAPI仕様書</a></div><div style='display:inline-block; margin-left:2px; left:2px; width:10px; height:10px; border-top:2px solid #00b8d4; border-right:2px solid #00b8d4; transparent;-webkit-transform:rotate(45deg); transform: rotate(45deg);'></div> </div> <h4 style='margin-top:30px; border-left: solid 4px #1B2F48; padding: 0.1em 0.5em; color:#1B2F48;'>共通仕様</h4> <div style='width:100%; margin:10px;'>   <p style='font-weight:bold; color:#616161;'>＜HTTPリクエストヘッダ＞</p>   <div style='display:table; margin-left:10px; background-color:#29659b;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff;'>項目</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; color:#fff;'>仕様</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>プロトコル</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>HTTP1.1/HTTPS</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>charset</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>UTF-8</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>content-type</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>application/json</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>domain_name</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>       本番環境：api.gmo-aozora.com</br>       開発環境：stg-api.gmo-aozora.com     </div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>メインURL</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>       https://{domain_name}/ganb/api/personal/{version}</br>       <span style='border-bottom:solid 1px;'>Version:1.x.x</span> の場合</br>       　https://api.gmo-aozora.com/ganb/api/personal/<span style='border-bottom:solid 1px;'>v1</span>     </div>   </div> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜リクエスト共通仕様＞</p>   <p style='padding-left:20px; font-weight:bold; color:#616161;'>NULLデータの扱い</p>   <p style='padding-left:40px;'>パラメータの値が空の場合、またはパラメータ自体が設定されていない場合、どちらもNULLとして扱います</p> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜レスポンス共通仕様＞</p>   <p style='padding-left:20px; font-weight:bold; color:#616161;'>NULLデータの扱い</p>   <ul>     <li>レスポンスデータ</li>       <ul>         <li style='list-style-type:none;'>レスポンスデータの値が空の場合または、レスポンスデータ自体が設定されない場合は「項目自体を設定しません」と記載</li>       </ul>     <li>配列</li>       <ul>         <li style='list-style-type:none;'>配列の要素の値が空の場合は「空のリスト」と記載</li>         <li style='list-style-type:none;'>配列自体が設定されない場合は「項目自体を設定しません」と記載</li>       </ul>   </ul> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜更新系APIに関する注意事項＞</p>   <ul>     <li style='list-style-type:none;'>更新系処理がタイムアウトとなった場合、処理自体は実行されている可能性がありますので、</li>     <li style='list-style-type:none;'>再実行を行う必要がある場合は必ず照会系の処理で実行状況を確認してから再実行を行ってください</li>   </ul> </div>   # noqa: E501

    OpenAPI spec version: 1.1.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ganb_personal_client.models.transfer import Transfer  # noqa: F401,E501


class TransferRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'str',
        'remitter_name': 'str',
        'transfer_designated_date': 'str',
        'transfer_date_holiday_code': 'str',
        'total_count': 'str',
        'total_amount': 'str',
        'apply_comment': 'str',
        'transfers': 'list[Transfer]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'remitter_name': 'remitterName',
        'transfer_designated_date': 'transferDesignatedDate',
        'transfer_date_holiday_code': 'transferDateHolidayCode',
        'total_count': 'totalCount',
        'total_amount': 'totalAmount',
        'apply_comment': 'applyComment',
        'transfers': 'transfers'
    }

    def __init__(self, account_id=None, remitter_name=None, transfer_designated_date=None, transfer_date_holiday_code=None, total_count=None, total_amount=None, apply_comment=None, transfers=None):  # noqa: E501
        """TransferRequest - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._remitter_name = None
        self._transfer_designated_date = None
        self._transfer_date_holiday_code = None
        self._total_count = None
        self._total_amount = None
        self._apply_comment = None
        self._transfers = None
        self.discriminator = None

        self.account_id = account_id
        if remitter_name is not None:
            self.remitter_name = remitter_name
        self.transfer_designated_date = transfer_designated_date
        if transfer_date_holiday_code is not None:
            self.transfer_date_holiday_code = transfer_date_holiday_code
        if total_count is not None:
            self.total_count = total_count
        if total_amount is not None:
            self.total_amount = total_amount
        if apply_comment is not None:
            self.apply_comment = apply_comment
        self.transfers = transfers

    @property
    def account_id(self):
        """Gets the account_id of this TransferRequest.  # noqa: E501

        口座ID 半角英数字 口座を識別するID   # noqa: E501

        :return: The account_id of this TransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TransferRequest.

        口座ID 半角英数字 口座を識別するID   # noqa: E501

        :param account_id: The account_id of this TransferRequest.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501
        if account_id is not None and len(account_id) > 29:
            raise ValueError("Invalid value for `account_id`, length must be less than or equal to `29`")  # noqa: E501
        if account_id is not None and len(account_id) < 12:
            raise ValueError("Invalid value for `account_id`, length must be greater than or equal to `12`")  # noqa: E501

        self._account_id = account_id

    @property
    def remitter_name(self):
        """Gets the remitter_name of this TransferRequest.  # noqa: E501

        振込依頼人名 半角文字 指定しない場合は口座名義がデフォルト値となります 振込許容文字を指定可 ただし、一部の非許容文字は、許容文字に変換を行います   # noqa: E501

        :return: The remitter_name of this TransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._remitter_name

    @remitter_name.setter
    def remitter_name(self, remitter_name):
        """Sets the remitter_name of this TransferRequest.

        振込依頼人名 半角文字 指定しない場合は口座名義がデフォルト値となります 振込許容文字を指定可 ただし、一部の非許容文字は、許容文字に変換を行います   # noqa: E501

        :param remitter_name: The remitter_name of this TransferRequest.  # noqa: E501
        :type: str
        """
        if remitter_name is not None and len(remitter_name) > 48:
            raise ValueError("Invalid value for `remitter_name`, length must be less than or equal to `48`")  # noqa: E501
        if remitter_name is not None and len(remitter_name) < 1:
            raise ValueError("Invalid value for `remitter_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._remitter_name = remitter_name

    @property
    def transfer_designated_date(self):
        """Gets the transfer_designated_date of this TransferRequest.  # noqa: E501

        振込指定日 半角文字 YYYY-MM-DD形式 振込対象の指定日 ただし、振込指定日が非営業日で、非営業日に実施できない振込（他行宛振込み）が振込情報に1件以上存在する場合、以下のとおりとなります ・「振込指定日休日コード」が1または省略の場合、振込指定日の翌営業日を振込対象の指定日となります ・「振込指定日休日コード」が2の場合、振込指定日の前営業日を振込対象の指定日となります ・「振込指定日休日コード」が3の場合、エラーとなり「400 Bad Request」を返却します   # noqa: E501

        :return: The transfer_designated_date of this TransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._transfer_designated_date

    @transfer_designated_date.setter
    def transfer_designated_date(self, transfer_designated_date):
        """Sets the transfer_designated_date of this TransferRequest.

        振込指定日 半角文字 YYYY-MM-DD形式 振込対象の指定日 ただし、振込指定日が非営業日で、非営業日に実施できない振込（他行宛振込み）が振込情報に1件以上存在する場合、以下のとおりとなります ・「振込指定日休日コード」が1または省略の場合、振込指定日の翌営業日を振込対象の指定日となります ・「振込指定日休日コード」が2の場合、振込指定日の前営業日を振込対象の指定日となります ・「振込指定日休日コード」が3の場合、エラーとなり「400 Bad Request」を返却します   # noqa: E501

        :param transfer_designated_date: The transfer_designated_date of this TransferRequest.  # noqa: E501
        :type: str
        """
        if transfer_designated_date is None:
            raise ValueError("Invalid value for `transfer_designated_date`, must not be `None`")  # noqa: E501
        if transfer_designated_date is not None and len(transfer_designated_date) > 10:
            raise ValueError("Invalid value for `transfer_designated_date`, length must be less than or equal to `10`")  # noqa: E501
        if transfer_designated_date is not None and len(transfer_designated_date) < 10:
            raise ValueError("Invalid value for `transfer_designated_date`, length must be greater than or equal to `10`")  # noqa: E501

        self._transfer_designated_date = transfer_designated_date

    @property
    def transfer_date_holiday_code(self):
        """Gets the transfer_date_holiday_code of this TransferRequest.  # noqa: E501

        振込指定日休日コード 半角数字 1：翌営業日、2：前営業日、3：エラー返却 省略可（省略した場合は1とみなします）   # noqa: E501

        :return: The transfer_date_holiday_code of this TransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._transfer_date_holiday_code

    @transfer_date_holiday_code.setter
    def transfer_date_holiday_code(self, transfer_date_holiday_code):
        """Sets the transfer_date_holiday_code of this TransferRequest.

        振込指定日休日コード 半角数字 1：翌営業日、2：前営業日、3：エラー返却 省略可（省略した場合は1とみなします）   # noqa: E501

        :param transfer_date_holiday_code: The transfer_date_holiday_code of this TransferRequest.  # noqa: E501
        :type: str
        """
        if transfer_date_holiday_code is not None and len(transfer_date_holiday_code) > 1:
            raise ValueError("Invalid value for `transfer_date_holiday_code`, length must be less than or equal to `1`")  # noqa: E501
        if transfer_date_holiday_code is not None and len(transfer_date_holiday_code) < 1:
            raise ValueError("Invalid value for `transfer_date_holiday_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._transfer_date_holiday_code = transfer_date_holiday_code

    @property
    def total_count(self):
        """Gets the total_count of this TransferRequest.  # noqa: E501

        合計件数 半角数字 1以上99件まで指定可能（0はエラー） 1件のみの場合は省略可（項目自体の設定が不要です）   # noqa: E501

        :return: The total_count of this TransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this TransferRequest.

        合計件数 半角数字 1以上99件まで指定可能（0はエラー） 1件のみの場合は省略可（項目自体の設定が不要です）   # noqa: E501

        :param total_count: The total_count of this TransferRequest.  # noqa: E501
        :type: str
        """
        if total_count is not None and len(total_count) > 6:
            raise ValueError("Invalid value for `total_count`, length must be less than or equal to `6`")  # noqa: E501
        if total_count is not None and len(total_count) < 1:
            raise ValueError("Invalid value for `total_count`, length must be greater than or equal to `1`")  # noqa: E501

        self._total_count = total_count

    @property
    def total_amount(self):
        """Gets the total_amount of this TransferRequest.  # noqa: E501

        合計金額 半角数字 1以上999,999,999,999円以下　数値のみで0、カンマ、マイナス不可 1件のみの場合は省略可（項目自体の設定が不要です）   # noqa: E501

        :return: The total_amount of this TransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this TransferRequest.

        合計金額 半角数字 1以上999,999,999,999円以下　数値のみで0、カンマ、マイナス不可 1件のみの場合は省略可（項目自体の設定が不要です）   # noqa: E501

        :param total_amount: The total_amount of this TransferRequest.  # noqa: E501
        :type: str
        """
        if total_amount is not None and len(total_amount) > 20:
            raise ValueError("Invalid value for `total_amount`, length must be less than or equal to `20`")  # noqa: E501
        if total_amount is not None and len(total_amount) < 1:
            raise ValueError("Invalid value for `total_amount`, length must be greater than or equal to `1`")  # noqa: E501

        self._total_amount = total_amount

    @property
    def apply_comment(self):
        """Gets the apply_comment of this TransferRequest.  # noqa: E501

        振込申請メモ（申請コメント） 全半角文字 項目自体の設定が不要 値を設定しても銀行で読み捨て   # noqa: E501

        :return: The apply_comment of this TransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._apply_comment

    @apply_comment.setter
    def apply_comment(self, apply_comment):
        """Sets the apply_comment of this TransferRequest.

        振込申請メモ（申請コメント） 全半角文字 項目自体の設定が不要 値を設定しても銀行で読み捨て   # noqa: E501

        :param apply_comment: The apply_comment of this TransferRequest.  # noqa: E501
        :type: str
        """
        if apply_comment is not None and len(apply_comment) > 20:
            raise ValueError("Invalid value for `apply_comment`, length must be less than or equal to `20`")  # noqa: E501
        if apply_comment is not None and len(apply_comment) < 1:
            raise ValueError("Invalid value for `apply_comment`, length must be greater than or equal to `1`")  # noqa: E501

        self._apply_comment = apply_comment

    @property
    def transfers(self):
        """Gets the transfers of this TransferRequest.  # noqa: E501

        振込情報 振込情報のリスト   # noqa: E501

        :return: The transfers of this TransferRequest.  # noqa: E501
        :rtype: list[Transfer]
        """
        return self._transfers

    @transfers.setter
    def transfers(self, transfers):
        """Sets the transfers of this TransferRequest.

        振込情報 振込情報のリスト   # noqa: E501

        :param transfers: The transfers of this TransferRequest.  # noqa: E501
        :type: list[Transfer]
        """
        if transfers is None:
            raise ValueError("Invalid value for `transfers`, must not be `None`")  # noqa: E501

        self._transfers = transfers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TransferRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransferRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
