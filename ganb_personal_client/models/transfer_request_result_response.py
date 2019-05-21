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


class TransferRequestResultResponse(object):
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
        'result_code': 'str',
        'apply_no': 'str',
        'apply_end_datetime': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'result_code': 'resultCode',
        'apply_no': 'applyNo',
        'apply_end_datetime': 'applyEndDatetime'
    }

    def __init__(self, account_id=None, result_code=None, apply_no=None, apply_end_datetime=None):  # noqa: E501
        """TransferRequestResultResponse - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._result_code = None
        self._apply_no = None
        self._apply_end_datetime = None
        self.discriminator = None

        self.account_id = account_id
        self.result_code = result_code
        self.apply_no = apply_no
        if apply_end_datetime is not None:
            self.apply_end_datetime = apply_end_datetime

    @property
    def account_id(self):
        """Gets the account_id of this TransferRequestResultResponse.  # noqa: E501

        口座ID 半角数字 口座を識別するID   # noqa: E501

        :return: The account_id of this TransferRequestResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TransferRequestResultResponse.

        口座ID 半角数字 口座を識別するID   # noqa: E501

        :param account_id: The account_id of this TransferRequestResultResponse.  # noqa: E501
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
    def result_code(self):
        """Gets the result_code of this TransferRequestResultResponse.  # noqa: E501

        結果コード 半角数字 1:完了　2：未完了　8：期限切   # noqa: E501

        :return: The result_code of this TransferRequestResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this TransferRequestResultResponse.

        結果コード 半角数字 1:完了　2：未完了　8：期限切   # noqa: E501

        :param result_code: The result_code of this TransferRequestResultResponse.  # noqa: E501
        :type: str
        """
        if result_code is None:
            raise ValueError("Invalid value for `result_code`, must not be `None`")  # noqa: E501
        if result_code is not None and len(result_code) > 1:
            raise ValueError("Invalid value for `result_code`, length must be less than or equal to `1`")  # noqa: E501
        if result_code is not None and len(result_code) < 1:
            raise ValueError("Invalid value for `result_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._result_code = result_code

    @property
    def apply_no(self):
        """Gets the apply_no of this TransferRequestResultResponse.  # noqa: E501

        受付番号（振込申請番号） 半角数字 すべての振込・総合振込で採番される、照会の基本単位となる番号   # noqa: E501

        :return: The apply_no of this TransferRequestResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._apply_no

    @apply_no.setter
    def apply_no(self, apply_no):
        """Sets the apply_no of this TransferRequestResultResponse.

        受付番号（振込申請番号） 半角数字 すべての振込・総合振込で採番される、照会の基本単位となる番号   # noqa: E501

        :param apply_no: The apply_no of this TransferRequestResultResponse.  # noqa: E501
        :type: str
        """
        if apply_no is None:
            raise ValueError("Invalid value for `apply_no`, must not be `None`")  # noqa: E501
        if apply_no is not None and len(apply_no) > 16:
            raise ValueError("Invalid value for `apply_no`, length must be less than or equal to `16`")  # noqa: E501
        if apply_no is not None and len(apply_no) < 16:
            raise ValueError("Invalid value for `apply_no`, length must be greater than or equal to `16`")  # noqa: E501

        self._apply_no = apply_no

    @property
    def apply_end_datetime(self):
        """Gets the apply_end_datetime of this TransferRequestResultResponse.  # noqa: E501

        振込依頼完了日時 半角文字 YYYY-MM-DDTHH:MM:SS+09:00形式 結果コードが、1:完了のときのみセット 振込申請番号の最も直近の依頼の完了日時を返却 それ以外は項目自体を設定しません   # noqa: E501

        :return: The apply_end_datetime of this TransferRequestResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._apply_end_datetime

    @apply_end_datetime.setter
    def apply_end_datetime(self, apply_end_datetime):
        """Sets the apply_end_datetime of this TransferRequestResultResponse.

        振込依頼完了日時 半角文字 YYYY-MM-DDTHH:MM:SS+09:00形式 結果コードが、1:完了のときのみセット 振込申請番号の最も直近の依頼の完了日時を返却 それ以外は項目自体を設定しません   # noqa: E501

        :param apply_end_datetime: The apply_end_datetime of this TransferRequestResultResponse.  # noqa: E501
        :type: str
        """
        if apply_end_datetime is not None and len(apply_end_datetime) > 25:
            raise ValueError("Invalid value for `apply_end_datetime`, length must be less than or equal to `25`")  # noqa: E501
        if apply_end_datetime is not None and len(apply_end_datetime) < 25:
            raise ValueError("Invalid value for `apply_end_datetime`, length must be greater than or equal to `25`")  # noqa: E501

        self._apply_end_datetime = apply_end_datetime

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
        if issubclass(TransferRequestResultResponse, dict):
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
        if not isinstance(other, TransferRequestResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
