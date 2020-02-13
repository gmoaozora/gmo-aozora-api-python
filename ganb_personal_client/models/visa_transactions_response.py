# coding: utf-8

import pprint
import re

import six

from ganb_personal_client.models.visa_transaction import VisaTransaction


class VisaTransactionsResponse(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'str',
        'date_from': 'str',
        'date_to': 'str',
        'base_date': 'str',
        'base_time': 'str',
        'has_next': 'bool',
        'next_item_key': 'str',
        'count': 'str',
        'visa_transactions': 'list[VisaTransaction]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'date_from': 'dateFrom',
        'date_to': 'dateTo',
        'base_date': 'baseDate',
        'base_time': 'baseTime',
        'has_next': 'hasNext',
        'next_item_key': 'nextItemKey',
        'count': 'count',
        'visa_transactions': 'visaTransactions'
    }

    def __init__(self, account_id=None, date_from=None, date_to=None, base_date=None, base_time=None, has_next=None, next_item_key=None, count=None, visa_transactions=None):
        """VisaTransactionsResponse - a model defined in Swagger"""

        self._account_id = None
        self._date_from = None
        self._date_to = None
        self._base_date = None
        self._base_time = None
        self._has_next = None
        self._next_item_key = None
        self._count = None
        self._visa_transactions = None
        self.discriminator = None

        self.account_id = account_id
        self.date_from = date_from
        self.date_to = date_to
        self.base_date = base_date
        self.base_time = base_time
        self.has_next = has_next
        if next_item_key is not None:
            self.next_item_key = next_item_key
        self.count = count
        if visa_transactions is not None:
            self.visa_transactions = visa_transactions

    @property
    def account_id(self):
        """Gets the account_id of this VisaTransactionsResponse.

        口座ID 半角英数字 口座を識別するID

        :return: The account_id of this VisaTransactionsResponse.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this VisaTransactionsResponse.

        口座ID 半角英数字 口座を識別するID

        :param account_id: The account_id of this VisaTransactionsResponse.
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")
        if account_id is not None and len(account_id) > 29:
            raise ValueError("Invalid value for `account_id`, length must be less than or equal to `29`")
        if account_id is not None and len(account_id) < 12:
            raise ValueError("Invalid value for `account_id`, length must be greater than or equal to `12`")

        self._account_id = account_id

    @property
    def date_from(self):
        """Gets the date_from of this VisaTransactionsResponse.

        対象期間From 半角文字 YYYY-MM-DD形式 リクエストに対象期間From、Toが設定されていない場合は当日日付が設定されます

        :return: The date_from of this VisaTransactionsResponse.
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this VisaTransactionsResponse.

        対象期間From 半角文字 YYYY-MM-DD形式 リクエストに対象期間From、Toが設定されていない場合は当日日付が設定されます

        :param date_from: The date_from of this VisaTransactionsResponse.
        :type: str
        """
        if date_from is None:
            raise ValueError("Invalid value for `date_from`, must not be `None`")
        if date_from is not None and len(date_from) > 10:
            raise ValueError("Invalid value for `date_from`, length must be less than or equal to `10`")
        if date_from is not None and len(date_from) < 10:
            raise ValueError("Invalid value for `date_from`, length must be greater than or equal to `10`")

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this VisaTransactionsResponse.

        対象期間To 半角文字 YYYY-MM-DD形式 リクエストに対象期間From、Toが設定されていない場合は当日日付が設定されます

        :return: The date_to of this VisaTransactionsResponse.
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this VisaTransactionsResponse.

        対象期間To 半角文字 YYYY-MM-DD形式 リクエストに対象期間From、Toが設定されていない場合は当日日付が設定されます

        :param date_to: The date_to of this VisaTransactionsResponse.
        :type: str
        """
        if date_to is None:
            raise ValueError("Invalid value for `date_to`, must not be `None`")
        if date_to is not None and len(date_to) > 10:
            raise ValueError("Invalid value for `date_to`, length must be less than or equal to `10`")
        if date_to is not None and len(date_to) < 10:
            raise ValueError("Invalid value for `date_to`, length must be greater than or equal to `10`")

        self._date_to = date_to

    @property
    def base_date(self):
        """Gets the base_date of this VisaTransactionsResponse.

        基準日 入出金明細を照会した基準日を示します YYYY-MM-DD形式

        :return: The base_date of this VisaTransactionsResponse.
        :rtype: str
        """
        return self._base_date

    @base_date.setter
    def base_date(self, base_date):
        """Sets the base_date of this VisaTransactionsResponse.

        基準日 入出金明細を照会した基準日を示します YYYY-MM-DD形式

        :param base_date: The base_date of this VisaTransactionsResponse.
        :type: str
        """
        if base_date is None:
            raise ValueError("Invalid value for `base_date`, must not be `None`")
        if base_date is not None and len(base_date) > 10:
            raise ValueError("Invalid value for `base_date`, length must be less than or equal to `10`")
        if base_date is not None and len(base_date) < 10:
            raise ValueError("Invalid value for `base_date`, length must be greater than or equal to `10`")

        self._base_date = base_date

    @property
    def base_time(self):
        """Gets the base_time of this VisaTransactionsResponse.

        基準時刻 入出金明細を照会した基準時刻を示します HH:MM:SS+09:00形式

        :return: The base_time of this VisaTransactionsResponse.
        :rtype: str
        """
        return self._base_time

    @base_time.setter
    def base_time(self, base_time):
        """Sets the base_time of this VisaTransactionsResponse.

        基準時刻 入出金明細を照会した基準時刻を示します HH:MM:SS+09:00形式

        :param base_time: The base_time of this VisaTransactionsResponse.
        :type: str
        """
        if base_time is None:
            raise ValueError("Invalid value for `base_time`, must not be `None`")
        if base_time is not None and len(base_time) > 14:
            raise ValueError("Invalid value for `base_time`, length must be less than or equal to `14`")
        if base_time is not None and len(base_time) < 14:
            raise ValueError("Invalid value for `base_time`, length must be greater than or equal to `14`")

        self._base_time = base_time

    @property
    def has_next(self):
        """Gets the has_next of this VisaTransactionsResponse.

        次明細フラグ ・true=次明細あり ・false=次明細なし

        :return: The has_next of this VisaTransactionsResponse.
        :rtype: bool
        """
        return self._has_next

    @has_next.setter
    def has_next(self, has_next):
        """Sets the has_next of this VisaTransactionsResponse.

        次明細フラグ ・true=次明細あり ・false=次明細なし

        :param has_next: The has_next of this VisaTransactionsResponse.
        :type: bool
        """
        if has_next is None:
            raise ValueError("Invalid value for `has_next`, must not be `None`")

        self._has_next = has_next

    @property
    def next_item_key(self):
        """Gets the next_item_key of this VisaTransactionsResponse.

        次明細キー 半角数字 次明細フラグがfalseの場合は、項目自体を設定しません

        :return: The next_item_key of this VisaTransactionsResponse.
        :rtype: str
        """
        return self._next_item_key

    @next_item_key.setter
    def next_item_key(self, next_item_key):
        """Sets the next_item_key of this VisaTransactionsResponse.

        次明細キー 半角数字 次明細フラグがfalseの場合は、項目自体を設定しません

        :param next_item_key: The next_item_key of this VisaTransactionsResponse.
        :type: str
        """
        if next_item_key is not None and len(next_item_key) > 24:
            raise ValueError("Invalid value for `next_item_key`, length must be less than or equal to `24`")
        if next_item_key is not None and len(next_item_key) < 1:
            raise ValueError("Invalid value for `next_item_key`, length must be greater than or equal to `1`")

        self._next_item_key = next_item_key

    @property
    def count(self):
        """Gets the count of this VisaTransactionsResponse.

        明細取得件数 半角数字

        :return: The count of this VisaTransactionsResponse.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this VisaTransactionsResponse.

        明細取得件数 半角数字

        :param count: The count of this VisaTransactionsResponse.
        :type: str
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")
        if count is not None and len(count) > 7:
            raise ValueError("Invalid value for `count`, length must be less than or equal to `7`")
        if count is not None and len(count) < 1:
            raise ValueError("Invalid value for `count`, length must be greater than or equal to `1`")

        self._count = count

    @property
    def visa_transactions(self):
        """Gets the visa_transactions of this VisaTransactionsResponse.

        Visaデビット取引明細情報リスト 該当する情報が無い場合は、空のリストを返却します

        :return: The visa_transactions of this VisaTransactionsResponse.
        :rtype: list[Transaction]
        """
        return self._visa_transactions

    @visa_transactions.setter
    def visa_transactions(self, visa_transactions):
        """Sets the visa_transactions of this VisaTransactionsResponse.

        Visaデビット取引明細情報リスト 該当する情報が無い場合は、空のリストを返却します

        :param visa_transactions: The visa_transactions of this VisaTransactionsResponse.
        :type: list[Transaction]
        """

        self._visa_transactions = visa_transactions

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
        if issubclass(VisaTransactionsResponse, dict):
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
        if not isinstance(other, VisaTransactionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
