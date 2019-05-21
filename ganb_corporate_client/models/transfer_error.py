# coding: utf-8

"""
    GMO Aozora Net Bank Open API

    <p>オープンAPI仕様書（PDF版）は下記リンクをご参照ください</p> <div>   <div style='display:inline-block;'><a style='text-decoration:none; font-weight:bold; color:#00b8d4;' href='https://gmo-aozora.com/business/service/api-specification.html' target='_blank'>オープンAPI仕様書</a></div><div style='display:inline-block; margin-left:2px; left:2px; width:10px; height:10px; border-top:2px solid #00b8d4; border-right:2px solid #00b8d4; transparent;-webkit-transform:rotate(45deg); transform: rotate(45deg);'></div> </div> <h4 style='margin-top:30px; border-left: solid 4px #1B2F48; padding: 0.1em 0.5em; color:#1B2F48;'>共通仕様</h4> <div style='width:100%; margin:10px;'>   <p style='font-weight:bold; color:#616161;'>＜HTTPリクエストヘッダ＞</p>   <div style='display:table; margin-left:10px; background-color:#29659b;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff;'>項目</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; color:#fff;'>仕様</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>プロトコル</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>HTTP1.1/HTTPS</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>charset</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>UTF-8</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>content-type</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>application/json</div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>domain_name</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>       本番環境：api.gmo-aozora.com</br>       開発環境：stg-api.gmo-aozora.com     </div>   </div>   <div style='display:table; margin-left:10px;'>     <div style='display:table-cell; min-width:130px; padding:9px; border:1px solid #fff; color:#fff; background-color:#29659b;'>メインURL</div>     <div style='display:table-cell; width:85%; padding:9px; border:1px solid #fff; background-color:#f8f8f8;'>       https://{domain_name}/ganb/api/corporation/{version}</br>       <span style='border-bottom:solid 1px;'>Version:1.x.x</span> の場合</br>       　https://api.gmo-aozora.com/ganb/api/corporation/<span style='border-bottom:solid 1px;'>v1</span>     </div>   </div> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜リクエスト共通仕様＞</p>   <p style='padding-left:20px; font-weight:bold; color:#616161;'>NULLデータの扱い</p>   <p style='padding-left:40px;'>パラメータの値が空の場合、またはパラメータ自体が設定されていない場合、どちらもNULLとして扱います</p> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜レスポンス共通仕様＞</p>   <p style='padding-left:20px; font-weight:bold; color:#616161;'>NULLデータの扱い</p>   <ul>     <li>レスポンスデータ</li>       <ul>         <li style='list-style-type:none;'>レスポンスデータの値が空の場合または、レスポンスデータ自体が設定されない場合は「項目自体を設定しません」と記載</li>       </ul>     <li>配列</li>       <ul>         <li style='list-style-type:none;'>配列の要素の値が空の場合は「空のリスト」と記載</li>         <li style='list-style-type:none;'>配列自体が設定されない場合は「項目自体を設定しません」と記載</li>       </ul>   </ul> </div> <div style='margin:20px 10px;'>   <p style='font-weight:bold; color:#616161;'>＜更新系APIに関する注意事項＞</p>   <ul>     <li style='list-style-type:none;'>更新系処理がタイムアウトとなった場合、処理自体は実行されている可能性がありますので、</li>     <li style='list-style-type:none;'>再実行を行う必要がある場合は必ず照会系の処理で実行状況を確認してから再実行を行ってください</li>   </ul> </div>   # noqa: E501

    OpenAPI spec version: 1.1.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ganb_corporate_client.models.error_detail import ErrorDetail  # noqa: F401,E501
from ganb_corporate_client.models.transfer_error_detail import TransferErrorDetail  # noqa: F401,E501


class TransferError(object):
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
        'error_code': 'str',
        'error_message': 'str',
        'error_details': 'list[ErrorDetail]',
        'transfer_error_details': 'list[TransferErrorDetail]'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'error_message': 'errorMessage',
        'error_details': 'errorDetails',
        'transfer_error_details': 'transferErrorDetails'
    }

    def __init__(self, error_code=None, error_message=None, error_details=None, transfer_error_details=None):  # noqa: E501
        """TransferError - a model defined in Swagger"""  # noqa: E501

        self._error_code = None
        self._error_message = None
        self._error_details = None
        self._transfer_error_details = None
        self.discriminator = None

        self.error_code = error_code
        self.error_message = error_message
        if error_details is not None:
            self.error_details = error_details
        if transfer_error_details is not None:
            self.transfer_error_details = transfer_error_details

    @property
    def error_code(self):
        """Gets the error_code of this TransferError.  # noqa: E501

        エラーコード 半角英数文字   # noqa: E501

        :return: The error_code of this TransferError.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this TransferError.

        エラーコード 半角英数文字   # noqa: E501

        :param error_code: The error_code of this TransferError.  # noqa: E501
        :type: str
        """
        if error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501
        if error_code is not None and len(error_code) > 10:
            raise ValueError("Invalid value for `error_code`, length must be less than or equal to `10`")  # noqa: E501
        if error_code is not None and len(error_code) < 1:
            raise ValueError("Invalid value for `error_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this TransferError.  # noqa: E501

        エラーメッセージ 全半角英数記号文字   # noqa: E501

        :return: The error_message of this TransferError.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this TransferError.

        エラーメッセージ 全半角英数記号文字   # noqa: E501

        :param error_message: The error_message of this TransferError.  # noqa: E501
        :type: str
        """
        if error_message is None:
            raise ValueError("Invalid value for `error_message`, must not be `None`")  # noqa: E501
        if error_message is not None and len(error_message) > 255:
            raise ValueError("Invalid value for `error_message`, length must be less than or equal to `255`")  # noqa: E501
        if error_message is not None and len(error_message) < 1:
            raise ValueError("Invalid value for `error_message`, length must be greater than or equal to `1`")  # noqa: E501

        self._error_message = error_message

    @property
    def error_details(self):
        """Gets the error_details of this TransferError.  # noqa: E501

        エラー詳細情報 該当する情報が無い場合は空のリストを返却   # noqa: E501

        :return: The error_details of this TransferError.  # noqa: E501
        :rtype: list[ErrorDetail]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this TransferError.

        エラー詳細情報 該当する情報が無い場合は空のリストを返却   # noqa: E501

        :param error_details: The error_details of this TransferError.  # noqa: E501
        :type: list[ErrorDetail]
        """

        self._error_details = error_details

    @property
    def transfer_error_details(self):
        """Gets the transfer_error_details of this TransferError.  # noqa: E501

        振込明細エラー情報 個別明細がエラーの場合のみ応答 該当する情報が無い場合は空のリストを返却   # noqa: E501

        :return: The transfer_error_details of this TransferError.  # noqa: E501
        :rtype: list[TransferErrorDetail]
        """
        return self._transfer_error_details

    @transfer_error_details.setter
    def transfer_error_details(self, transfer_error_details):
        """Sets the transfer_error_details of this TransferError.

        振込明細エラー情報 個別明細がエラーの場合のみ応答 該当する情報が無い場合は空のリストを返却   # noqa: E501

        :param transfer_error_details: The transfer_error_details of this TransferError.  # noqa: E501
        :type: list[TransferErrorDetail]
        """

        self._transfer_error_details = transfer_error_details

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
        if issubclass(TransferError, dict):
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
        if not isinstance(other, TransferError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
