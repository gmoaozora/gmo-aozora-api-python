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

from ganb_corporate_client.models.va import Va  # noqa: F401,E501


class VaIssueResponse(object):
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
        'va_type_code': 'str',
        'va_type_name': 'str',
        'expire_date_time': 'str',
        'va_holder_name_kana': 'str',
        'va_list': 'list[Va]'
    }

    attribute_map = {
        'va_type_code': 'vaTypeCode',
        'va_type_name': 'vaTypeName',
        'expire_date_time': 'expireDateTime',
        'va_holder_name_kana': 'vaHolderNameKana',
        'va_list': 'vaList'
    }

    def __init__(self, va_type_code=None, va_type_name=None, expire_date_time=None, va_holder_name_kana=None, va_list=None):  # noqa: E501
        """VaIssueResponse - a model defined in Swagger"""  # noqa: E501

        self._va_type_code = None
        self._va_type_name = None
        self._expire_date_time = None
        self._va_holder_name_kana = None
        self._va_list = None
        self.discriminator = None

        self.va_type_code = va_type_code
        self.va_type_name = va_type_name
        if expire_date_time is not None:
            self.expire_date_time = expire_date_time
        self.va_holder_name_kana = va_holder_name_kana
        self.va_list = va_list

    @property
    def va_type_code(self):
        """Gets the va_type_code of this VaIssueResponse.  # noqa: E501

        振込入金口座　種類コード 半角数字 ・1=期限型 ・2=継続型   # noqa: E501

        :return: The va_type_code of this VaIssueResponse.  # noqa: E501
        :rtype: str
        """
        return self._va_type_code

    @va_type_code.setter
    def va_type_code(self, va_type_code):
        """Sets the va_type_code of this VaIssueResponse.

        振込入金口座　種類コード 半角数字 ・1=期限型 ・2=継続型   # noqa: E501

        :param va_type_code: The va_type_code of this VaIssueResponse.  # noqa: E501
        :type: str
        """
        if va_type_code is None:
            raise ValueError("Invalid value for `va_type_code`, must not be `None`")  # noqa: E501
        if va_type_code is not None and len(va_type_code) > 1:
            raise ValueError("Invalid value for `va_type_code`, length must be less than or equal to `1`")  # noqa: E501
        if va_type_code is not None and len(va_type_code) < 1:
            raise ValueError("Invalid value for `va_type_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._va_type_code = va_type_code

    @property
    def va_type_name(self):
        """Gets the va_type_name of this VaIssueResponse.  # noqa: E501

        振込入金口座　種類名 全角文字 振込入金口座　種類コードの名称   # noqa: E501

        :return: The va_type_name of this VaIssueResponse.  # noqa: E501
        :rtype: str
        """
        return self._va_type_name

    @va_type_name.setter
    def va_type_name(self, va_type_name):
        """Sets the va_type_name of this VaIssueResponse.

        振込入金口座　種類名 全角文字 振込入金口座　種類コードの名称   # noqa: E501

        :param va_type_name: The va_type_name of this VaIssueResponse.  # noqa: E501
        :type: str
        """
        if va_type_name is None:
            raise ValueError("Invalid value for `va_type_name`, must not be `None`")  # noqa: E501
        if va_type_name is not None and len(va_type_name) > 10:
            raise ValueError("Invalid value for `va_type_name`, length must be less than or equal to `10`")  # noqa: E501
        if va_type_name is not None and len(va_type_name) < 1:
            raise ValueError("Invalid value for `va_type_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._va_type_name = va_type_name

    @property
    def expire_date_time(self):
        """Gets the expire_date_time of this VaIssueResponse.  # noqa: E501

        有効期限日時 半角文字 YYYY-MM-DDTHH:MM:SS+09:00形式 振込入金口座種別コードが「2=継続型」の場合は、項目自体を設定しません   # noqa: E501

        :return: The expire_date_time of this VaIssueResponse.  # noqa: E501
        :rtype: str
        """
        return self._expire_date_time

    @expire_date_time.setter
    def expire_date_time(self, expire_date_time):
        """Sets the expire_date_time of this VaIssueResponse.

        有効期限日時 半角文字 YYYY-MM-DDTHH:MM:SS+09:00形式 振込入金口座種別コードが「2=継続型」の場合は、項目自体を設定しません   # noqa: E501

        :param expire_date_time: The expire_date_time of this VaIssueResponse.  # noqa: E501
        :type: str
        """
        if expire_date_time is not None and len(expire_date_time) > 25:
            raise ValueError("Invalid value for `expire_date_time`, length must be less than or equal to `25`")  # noqa: E501
        if expire_date_time is not None and len(expire_date_time) < 25:
            raise ValueError("Invalid value for `expire_date_time`, length must be greater than or equal to `25`")  # noqa: E501

        self._expire_date_time = expire_date_time

    @property
    def va_holder_name_kana(self):
        """Gets the va_holder_name_kana of this VaIssueResponse.  # noqa: E501

        振込入金口座名義カナ 半角文字   # noqa: E501

        :return: The va_holder_name_kana of this VaIssueResponse.  # noqa: E501
        :rtype: str
        """
        return self._va_holder_name_kana

    @va_holder_name_kana.setter
    def va_holder_name_kana(self, va_holder_name_kana):
        """Sets the va_holder_name_kana of this VaIssueResponse.

        振込入金口座名義カナ 半角文字   # noqa: E501

        :param va_holder_name_kana: The va_holder_name_kana of this VaIssueResponse.  # noqa: E501
        :type: str
        """
        if va_holder_name_kana is None:
            raise ValueError("Invalid value for `va_holder_name_kana`, must not be `None`")  # noqa: E501
        if va_holder_name_kana is not None and len(va_holder_name_kana) > 40:
            raise ValueError("Invalid value for `va_holder_name_kana`, length must be less than or equal to `40`")  # noqa: E501
        if va_holder_name_kana is not None and len(va_holder_name_kana) < 1:
            raise ValueError("Invalid value for `va_holder_name_kana`, length must be greater than or equal to `1`")  # noqa: E501

        self._va_holder_name_kana = va_holder_name_kana

    @property
    def va_list(self):
        """Gets the va_list of this VaIssueResponse.  # noqa: E501

        振込入金口座リスト  # noqa: E501

        :return: The va_list of this VaIssueResponse.  # noqa: E501
        :rtype: list[Va]
        """
        return self._va_list

    @va_list.setter
    def va_list(self, va_list):
        """Sets the va_list of this VaIssueResponse.

        振込入金口座リスト  # noqa: E501

        :param va_list: The va_list of this VaIssueResponse.  # noqa: E501
        :type: list[Va]
        """
        if va_list is None:
            raise ValueError("Invalid value for `va_list`, must not be `None`")  # noqa: E501

        self._va_list = va_list

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
        if issubclass(VaIssueResponse, dict):
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
        if not isinstance(other, VaIssueResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other