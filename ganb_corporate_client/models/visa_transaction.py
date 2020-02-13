# coding: utf-8

import pprint
import re

import six


class VisaTransaction(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'use_date': 'str',
        'use_content': 'str',
        'amount': 'str',
        'local_currency_amount': 'str',
        'conversion_rate': 'str',
        'approval_number': 'str',
        'visa_status': 'str',
        'currency_code': 'str',
        'atm_comission': 'str'
    }

    attribute_map = {
        'use_date': 'useDate',
        'use_content': 'useContent',
        'amount': 'amount',
        'local_currency_amount': 'localCurrencyAmount',
        'conversion_rate': 'conversionRate',
        'approval_number': 'approvalNumber',
        'visa_status': 'visaStatus',
        'currency_code': 'currencyCode',
        'atm_comission': 'atmComission',
    }

    def __init__(self, use_date=None, use_content=None, amount=None, local_currency_amount=None, conversion_rate=None, approval_number=None, visa_status=None, currency_code=None, atm_comission=None):
        """VisaTransaction - a model defined in Swagger"""

        self._use_date = None
        self._use_content = None
        self._amount = None
        self._local_currency_amount = None
        self._conversion_rate = None
        self._approval_number = None
        self._visa_status = None
        self._currency_code = None
        self._atm_comission = None
        self.discriminator = None

        if use_date is not None:
            self.use_date = use_date
        if use_content is not None:
            self.use_content = use_content
        if amount is not None:
            self.amount = amount
        if local_currency_amount is not None:
            self.local_currency_amount = local_currency_amount
        if conversion_rate is not None:
            self.conversion_rate = conversion_rate
        if approval_number is not None:
            self.approval_number = approval_number
        if visa_status is not None:
            self.visa_status = visa_status
        if currency_code is not None:
            self.currency_code = currency_code
        if atm_comission is not None:
            self.atm_comission = atm_comission

    @property
    def use_date(self):
        """Gets the use_date of this VisaTransaction.

        利用日 半角文字 YYYY-MM-DD形式

        :return: The use_date of this VisaTransaction.
        :rtype: str
        """
        return self._use_date

    @use_date.setter
    def use_date(self, use_date):
        """Sets the use_date of this VisaTransaction.

        利用日 半角文字 YYYY-MM-DD形式

        :param use_date: The use_date of this VisaTransaction.
        :type: str
        """
        if use_date is None:
            raise ValueError("Invalid value for `use_date`, must not be `None`")
        if use_date is not None and len(use_date) > 10:
            raise ValueError("Invalid value for `use_date`, length must be less than or equal to `10`")
        if use_date is not None and len(use_date) < 10:
            raise ValueError("Invalid value for `use_date`, length must be greater than or equal to `10`")

        self._use_date = use_date

    @property
    def use_content(self):
        """Gets the use_content of this VisaTransaction.

        利用内容 全半角文字

        :return: The use_content of this VisaTransaction.
        :rtype: str
        """
        return self._use_content

    @use_content.setter
    def use_content(self, use_content):
        """Sets the use_content of this VisaTransaction.

        利用内容 全半角文字

        :param use_content: The use_content of this VisaTransaction.
        :type: str
        """
        if use_content is None:
            raise ValueError("Invalid value for `use_content`, must not be `None`")
        if use_content is not None and len(use_content) > 120:
            raise ValueError("Invalid value for `use_content`, length must be less than or equal to `120`")
        if use_content is not None and len(use_content) < 1:
            raise ValueError("Invalid value for `use_content`, length must be greater than or equal to `1`")

        self._use_content = use_content

    @property
    def amount(self):
        """Gets the amount of this VisaTransaction.

        利用金額 半角数字 マイナス含む 円貨金額

        :return: The amount of this VisaTransaction.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this VisaTransaction.

        利用金額 半角数字 マイナス含む 円貨金額

        :param amount: The amount of this VisaTransaction.
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")
        if amount is not None and len(amount) > 20:
            raise ValueError("Invalid value for `amount`, length must be less than or equal to `20`")
        if amount is not None and len(amount) < 1:
            raise ValueError("Invalid value for `amount`, length must be greater than or equal to `1`")

        self._amount = amount

    @property
    def local_currency_amount(self):
        """Gets the local_currency_amount of this VisaTransaction.

        現地通貨金額 半角数字 小数部最大6桁 マイナス含む 国内利用の場合は項目自体を設定しません

        :return: The local_currency_amount of this VisaTransaction.
        :rtype: str
        """
        return self._local_currency_amount

    @local_currency_amount.setter
    def local_currency_amount(self, local_currency_amount):
        """Sets the local_currency_amount of this VisaTransaction.

        現地通貨金額 半角数字 小数部最大6桁 マイナス含む 国内利用の場合は項目自体を設定しません

        :param local_currency_amount: The local_currency_amount of this VisaTransaction.
        :type: str
        """
        if local_currency_amount is not None and len(local_currency_amount) > 20:
            raise ValueError("Invalid value for `local_currency_amount`, length must be less than or equal to `20`")
        if local_currency_amount is not None and len(local_currency_amount) < 3:
            raise ValueError("Invalid value for `local_currency_amount`, length must be greater than or equal to `3`")

        self._local_currency_amount = local_currency_amount

    @property
    def conversion_rate(self):
        """Gets the conversion_rate of this VisaTransaction.

        円換算レート 半角数字 小数部最大6桁 マイナス含む 国内利用の場合は項目自体を設定しません

        :return: The conversion_rate of this VisaTransaction.
        :rtype: str
        """
        return self._conversion_rate

    @conversion_rate.setter
    def conversion_rate(self, conversion_rate):
        """Sets the conversion_rate of this VisaTransaction.

        円換算レート 半角数字 小数部最大6桁 マイナス含む 国内利用の場合は項目自体を設定しません

        :param conversion_rate: The conversion_rate of this VisaTransaction.
        :type: str
        """
        if conversion_rate is None:
            raise ValueError("Invalid value for `conversion_rate`, must not be `None`")
        if conversion_rate is not None and len(conversion_rate) > 14:
            raise ValueError("Invalid value for `conversion_rate`, length must be less than or equal to `14`")
        if conversion_rate is not None and len(conversion_rate) < 3:
            raise ValueError("Invalid value for `conversion_rate`, length must be greater than or equal to `3`")

        self._conversion_rate = conversion_rate

    @property
    def approval_number(self):
        """Gets the approval_number of this VisaTransaction.

        承認番号 半角数字

        :return: The approval_number of this VisaTransaction.
        :rtype: str
        """
        return self._approval_number

    @approval_number.setter
    def approval_number(self, approval_number):
        """Sets the approval_number of this VisaTransaction.

        承認番号 半角数字

        :param approval_number: The approval_number of this VisaTransaction.
        :type: str
        """
        if approval_number is not None and len(approval_number) > 6:
            raise ValueError("Invalid value for `approval_number`, length must be less than or equal to `6`")
        if approval_number is not None and len(approval_number) < 6:
            raise ValueError("Invalid value for `approval_number`, length must be greater than or equal to `6`")

        self._approval_number = approval_number

    @property
    def visa_status(self):
        """Gets the visa_status of this VisaTransaction.

        ステータス 半角数字
        1:確定・・・決済として完了している状態 2:未確定・・・加盟店からの情報によりお客様の口座から資金を引き落としていますが、決済としては完了していない状態 3:取消済・・・取消を行った状態

        :return: The visa_status of this VisaTransaction.
        :rtype: str
        """
        return self._visa_status

    @visa_status.setter
    def visa_status(self, visa_status):
        """Sets the visa_status of this VisaTransaction.

        ステータス 半角数字
        1:確定・・・決済として完了している状態 2:未確定・・・加盟店からの情報によりお客様の口座から資金を引き落としていますが、決済としては完了していない状態 3:取消済・・・取消を行った状態

        :param visa_status: The visa_status of this VisaTransaction.
        :type: str
        """
        if visa_status is not None and len(visa_status) > 1:
            raise ValueError("Invalid value for `visa_status`, length must be less than or equal to `1`")
        if visa_status is not None and len(visa_status) < 1:
            raise ValueError("Invalid value for `visa_status`, length must be greater than or equal to `1`")

        self._visa_status = visa_status
        
    @property
    def currency_code(self):
        """Gets the currency_code of this VisaTransaction.

        通貨コード 半角文字 ISO4217準拠した通貨コード 国内利用の場合は項目自体を設定しません

        :return: The currency_code of this VisaTransaction.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this VisaTransaction.

        通貨コード 半角文字 ISO4217準拠した通貨コード 国内利用の場合は項目自体を設定しません

        :param currency_code: The currency_code of this VisaTransaction.
        :type: str
        """
        if currency_code is not None and len(currency_code) > 3:
            raise ValueError("Invalid value for `currency_code`, length must be less than or equal to `3`")
        if currency_code is not None and len(currency_code) < 3:
            raise ValueError("Invalid value for `currency_code`, length must be greater than or equal to `3`")

        self._currency_code = currency_code
        
    @property
    def atm_comission(self):
        """Gets the atm_comission of this VisaTransaction.

        ATM手数料 半角数字 小数部最大6桁 マイナス含む 現地通貨金額でのATM手数料 国内利用の場合または、ATM手数料自体が発生していない場合は項目自体を設定しません

        :return: The atm_comission of this VisaTransaction.
        :rtype: str
        """
        return self._atm_comission

    @atm_comission.setter
    def atm_comission(self, atm_comission):
        """Sets the atm_comission of this VisaTransaction.

        ATM手数料 半角数字 小数部最大6桁 マイナス含む 現地通貨金額でのATM手数料 国内利用の場合または、ATM手数料自体が発生していない場合は項目自体を設定しません

        :param atm_comission: The atm_comission of this VisaTransaction.
        :type: str
        """
        if atm_comission is not None and len(atm_comission) > 20:
            raise ValueError("Invalid value for `atm_comission`, length must be less than or equal to `20`")
        if atm_comission is not None and len(atm_comission) < 3:
            raise ValueError("Invalid value for `atm_comission`, length must be greater than or equal to `3`")

        self._atm_comission = atm_comission

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
        if issubclass(VisaTransaction, dict):
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
        if not isinstance(other, VisaTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
