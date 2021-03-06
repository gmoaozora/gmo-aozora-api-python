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


class Transaction(object):
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
        'transaction_date': 'str',
        'value_date': 'str',
        'transaction_type': 'str',
        'amount': 'str',
        'remarks': 'str',
        'balance': 'str',
        'item_key': 'str'
    }

    attribute_map = {
        'transaction_date': 'transactionDate',
        'value_date': 'valueDate',
        'transaction_type': 'transactionType',
        'amount': 'amount',
        'remarks': 'remarks',
        'balance': 'balance',
        'item_key': 'itemKey'
    }

    def __init__(self, transaction_date=None, value_date=None, transaction_type=None, amount=None, remarks=None, balance=None, item_key=None):  # noqa: E501
        """Transaction - a model defined in Swagger"""  # noqa: E501

        self._transaction_date = None
        self._value_date = None
        self._transaction_type = None
        self._amount = None
        self._remarks = None
        self._balance = None
        self._item_key = None
        self.discriminator = None

        self.transaction_date = transaction_date
        self.value_date = value_date
        self.transaction_type = transaction_type
        self.amount = amount
        if remarks is not None:
            self.remarks = remarks
        self.balance = balance
        if item_key is not None:
            self.item_key = item_key

    @property
    def transaction_date(self):
        """Gets the transaction_date of this Transaction.  # noqa: E501

        取引日 半角文字 YYYY-MM-DD形式   # noqa: E501

        :return: The transaction_date of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this Transaction.

        取引日 半角文字 YYYY-MM-DD形式   # noqa: E501

        :param transaction_date: The transaction_date of this Transaction.  # noqa: E501
        :type: str
        """
        if transaction_date is None:
            raise ValueError("Invalid value for `transaction_date`, must not be `None`")  # noqa: E501
        if transaction_date is not None and len(transaction_date) > 10:
            raise ValueError("Invalid value for `transaction_date`, length must be less than or equal to `10`")  # noqa: E501
        if transaction_date is not None and len(transaction_date) < 10:
            raise ValueError("Invalid value for `transaction_date`, length must be greater than or equal to `10`")  # noqa: E501

        self._transaction_date = transaction_date

    @property
    def value_date(self):
        """Gets the value_date of this Transaction.  # noqa: E501

        起算日 半角文字 YYYY-MM-DD形式   # noqa: E501

        :return: The value_date of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._value_date

    @value_date.setter
    def value_date(self, value_date):
        """Sets the value_date of this Transaction.

        起算日 半角文字 YYYY-MM-DD形式   # noqa: E501

        :param value_date: The value_date of this Transaction.  # noqa: E501
        :type: str
        """
        if value_date is None:
            raise ValueError("Invalid value for `value_date`, must not be `None`")  # noqa: E501
        if value_date is not None and len(value_date) > 10:
            raise ValueError("Invalid value for `value_date`, length must be less than or equal to `10`")  # noqa: E501
        if value_date is not None and len(value_date) < 10:
            raise ValueError("Invalid value for `value_date`, length must be greater than or equal to `10`")  # noqa: E501

        self._value_date = value_date

    @property
    def transaction_type(self):
        """Gets the transaction_type of this Transaction.  # noqa: E501

        入払コード 半角数字 ・1=入金 ・2=出金   # noqa: E501

        :return: The transaction_type of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this Transaction.

        入払コード 半角数字 ・1=入金 ・2=出金   # noqa: E501

        :param transaction_type: The transaction_type of this Transaction.  # noqa: E501
        :type: str
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501
        if transaction_type is not None and len(transaction_type) > 1:
            raise ValueError("Invalid value for `transaction_type`, length must be less than or equal to `1`")  # noqa: E501
        if transaction_type is not None and len(transaction_type) < 1:
            raise ValueError("Invalid value for `transaction_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def amount(self):
        """Gets the amount of this Transaction.  # noqa: E501

        取引金額 半角数字　マイナス含む   # noqa: E501

        :return: The amount of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Transaction.

        取引金額 半角数字　マイナス含む   # noqa: E501

        :param amount: The amount of this Transaction.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501
        if amount is not None and len(amount) > 20:
            raise ValueError("Invalid value for `amount`, length must be less than or equal to `20`")  # noqa: E501
        if amount is not None and len(amount) < 1:
            raise ValueError("Invalid value for `amount`, length must be greater than or equal to `1`")  # noqa: E501

        self._amount = amount

    @property
    def remarks(self):
        """Gets the remarks of this Transaction.  # noqa: E501

        摘要内容 全半角文字 該当データがない場合は項目自体を設定しません   # noqa: E501

        :return: The remarks of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this Transaction.

        摘要内容 全半角文字 該当データがない場合は項目自体を設定しません   # noqa: E501

        :param remarks: The remarks of this Transaction.  # noqa: E501
        :type: str
        """
        if remarks is not None and len(remarks) > 255:
            raise ValueError("Invalid value for `remarks`, length must be less than or equal to `255`")  # noqa: E501
        if remarks is not None and len(remarks) < 1:
            raise ValueError("Invalid value for `remarks`, length must be greater than or equal to `1`")  # noqa: E501

        self._remarks = remarks

    @property
    def balance(self):
        """Gets the balance of this Transaction.  # noqa: E501

        取引後残高 半角数字　マイナス含む   # noqa: E501

        :return: The balance of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Transaction.

        取引後残高 半角数字　マイナス含む   # noqa: E501

        :param balance: The balance of this Transaction.  # noqa: E501
        :type: str
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501
        if balance is not None and len(balance) > 20:
            raise ValueError("Invalid value for `balance`, length must be less than or equal to `20`")  # noqa: E501
        if balance is not None and len(balance) < 1:
            raise ValueError("Invalid value for `balance`, length must be greater than or equal to `1`")  # noqa: E501

        self._balance = balance

    @property
    def item_key(self):
        """Gets the item_key of this Transaction.  # noqa: E501

        明細キー 半角数字 口座の科目が01=普通預金（有利息）または02=普通預金（決済用）の場合は口座ID毎に設定される明細キー（明細データtimestamp（μs）） 該当データがない場合は項目自体を設定しません  # noqa: E501

        :return: The item_key of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._item_key

    @item_key.setter
    def item_key(self, item_key):
        """Sets the item_key of this Transaction.

        明細キー 半角数字 口座の科目が01=普通預金（有利息）または02=普通預金（決済用）の場合は口座ID毎に設定される明細キー（明細データtimestamp（μs）） 該当データがない場合は項目自体を設定しません  # noqa: E501

        :param item_key: The item_key of this Transaction.  # noqa: E501
        :type: str
        """
        if item_key is not None and len(item_key) > 24:
            raise ValueError("Invalid value for `item_key`, length must be less than or equal to `24`")  # noqa: E501
        if item_key is not None and len(item_key) < 1:
            raise ValueError("Invalid value for `item_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._item_key = item_key

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
        if issubclass(Transaction, dict):
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
        if not isinstance(other, Transaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
