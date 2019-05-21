# coding: utf-8

"""
    GMO Aozora Net Bank Open API

    <p>Ph2.5向けに作成したもの</p>   # noqa: E501

    OpenAPI spec version: 1.1.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Account(object):
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
        'ra_id': 'str',
        'ra_branch_code': 'str',
        'ra_branch_name_kana': 'str',
        'ra_account_number': 'str',
        'ra_holder_name': 'str',
        'base_date': 'str',
        'base_time': 'str'
    }

    attribute_map = {
        'ra_id': 'raId',
        'ra_branch_code': 'raBranchCode',
        'ra_branch_name_kana': 'raBranchNameKana',
        'ra_account_number': 'raAccountNumber',
        'ra_holder_name': 'raHolderName',
        'base_date': 'baseDate',
        'base_time': 'baseTime'
    }

    def __init__(self, ra_id=None, ra_branch_code=None, ra_branch_name_kana=None, ra_account_number=None, ra_holder_name=None, base_date=None, base_time=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501

        self._ra_id = None
        self._ra_branch_code = None
        self._ra_branch_name_kana = None
        self._ra_account_number = None
        self._ra_holder_name = None
        self._base_date = None
        self._base_time = None
        self.discriminator = None

        self.ra_id = ra_id
        self.ra_branch_code = ra_branch_code
        self.ra_branch_name_kana = ra_branch_name_kana
        self.ra_account_number = ra_account_number
        self.ra_holder_name = ra_holder_name
        self.base_date = base_date
        self.base_time = base_time

    @property
    def ra_id(self):
        """Gets the ra_id of this Account.  # noqa: E501

        入金口座ID 半角数字 入金先の口座を識別するID   # noqa: E501

        :return: The ra_id of this Account.  # noqa: E501
        :rtype: str
        """
        return self._ra_id

    @ra_id.setter
    def ra_id(self, ra_id):
        """Sets the ra_id of this Account.

        入金口座ID 半角数字 入金先の口座を識別するID   # noqa: E501

        :param ra_id: The ra_id of this Account.  # noqa: E501
        :type: str
        """
        if ra_id is None:
            raise ValueError("Invalid value for `ra_id`, must not be `None`")  # noqa: E501
        if ra_id is not None and len(ra_id) > 29:
            raise ValueError("Invalid value for `ra_id`, length must be less than or equal to `29`")  # noqa: E501
        if ra_id is not None and len(ra_id) < 12:
            raise ValueError("Invalid value for `ra_id`, length must be greater than or equal to `12`")  # noqa: E501

        self._ra_id = ra_id

    @property
    def ra_branch_code(self):
        """Gets the ra_branch_code of this Account.  # noqa: E501

        入金口座　支店コード 半角数字   # noqa: E501

        :return: The ra_branch_code of this Account.  # noqa: E501
        :rtype: str
        """
        return self._ra_branch_code

    @ra_branch_code.setter
    def ra_branch_code(self, ra_branch_code):
        """Sets the ra_branch_code of this Account.

        入金口座　支店コード 半角数字   # noqa: E501

        :param ra_branch_code: The ra_branch_code of this Account.  # noqa: E501
        :type: str
        """
        if ra_branch_code is None:
            raise ValueError("Invalid value for `ra_branch_code`, must not be `None`")  # noqa: E501
        if ra_branch_code is not None and len(ra_branch_code) > 3:
            raise ValueError("Invalid value for `ra_branch_code`, length must be less than or equal to `3`")  # noqa: E501
        if ra_branch_code is not None and len(ra_branch_code) < 3:
            raise ValueError("Invalid value for `ra_branch_code`, length must be greater than or equal to `3`")  # noqa: E501

        self._ra_branch_code = ra_branch_code

    @property
    def ra_branch_name_kana(self):
        """Gets the ra_branch_name_kana of this Account.  # noqa: E501

        半角文字   # noqa: E501

        :return: The ra_branch_name_kana of this Account.  # noqa: E501
        :rtype: str
        """
        return self._ra_branch_name_kana

    @ra_branch_name_kana.setter
    def ra_branch_name_kana(self, ra_branch_name_kana):
        """Sets the ra_branch_name_kana of this Account.

        半角文字   # noqa: E501

        :param ra_branch_name_kana: The ra_branch_name_kana of this Account.  # noqa: E501
        :type: str
        """
        if ra_branch_name_kana is None:
            raise ValueError("Invalid value for `ra_branch_name_kana`, must not be `None`")  # noqa: E501
        if ra_branch_name_kana is not None and len(ra_branch_name_kana) > 15:
            raise ValueError("Invalid value for `ra_branch_name_kana`, length must be less than or equal to `15`")  # noqa: E501
        if ra_branch_name_kana is not None and len(ra_branch_name_kana) < 1:
            raise ValueError("Invalid value for `ra_branch_name_kana`, length must be greater than or equal to `1`")  # noqa: E501

        self._ra_branch_name_kana = ra_branch_name_kana

    @property
    def ra_account_number(self):
        """Gets the ra_account_number of this Account.  # noqa: E501

        半角数字   # noqa: E501

        :return: The ra_account_number of this Account.  # noqa: E501
        :rtype: str
        """
        return self._ra_account_number

    @ra_account_number.setter
    def ra_account_number(self, ra_account_number):
        """Sets the ra_account_number of this Account.

        半角数字   # noqa: E501

        :param ra_account_number: The ra_account_number of this Account.  # noqa: E501
        :type: str
        """
        if ra_account_number is None:
            raise ValueError("Invalid value for `ra_account_number`, must not be `None`")  # noqa: E501
        if ra_account_number is not None and len(ra_account_number) > 7:
            raise ValueError("Invalid value for `ra_account_number`, length must be less than or equal to `7`")  # noqa: E501
        if ra_account_number is not None and len(ra_account_number) < 7:
            raise ValueError("Invalid value for `ra_account_number`, length must be greater than or equal to `7`")  # noqa: E501

        self._ra_account_number = ra_account_number

    @property
    def ra_holder_name(self):
        """Gets the ra_holder_name of this Account.  # noqa: E501

        全角文字   # noqa: E501

        :return: The ra_holder_name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._ra_holder_name

    @ra_holder_name.setter
    def ra_holder_name(self, ra_holder_name):
        """Sets the ra_holder_name of this Account.

        全角文字   # noqa: E501

        :param ra_holder_name: The ra_holder_name of this Account.  # noqa: E501
        :type: str
        """
        if ra_holder_name is None:
            raise ValueError("Invalid value for `ra_holder_name`, must not be `None`")  # noqa: E501
        if ra_holder_name is not None and len(ra_holder_name) > 48:
            raise ValueError("Invalid value for `ra_holder_name`, length must be less than or equal to `48`")  # noqa: E501
        if ra_holder_name is not None and len(ra_holder_name) < 1:
            raise ValueError("Invalid value for `ra_holder_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._ra_holder_name = ra_holder_name

    @property
    def base_date(self):
        """Gets the base_date of this Account.  # noqa: E501

        基準日 半角文字 応答日付、もしくは入金明細の基準日を示す。 YYYY-MM-DD形式   # noqa: E501

        :return: The base_date of this Account.  # noqa: E501
        :rtype: str
        """
        return self._base_date

    @base_date.setter
    def base_date(self, base_date):
        """Sets the base_date of this Account.

        基準日 半角文字 応答日付、もしくは入金明細の基準日を示す。 YYYY-MM-DD形式   # noqa: E501

        :param base_date: The base_date of this Account.  # noqa: E501
        :type: str
        """
        if base_date is None:
            raise ValueError("Invalid value for `base_date`, must not be `None`")  # noqa: E501
        if base_date is not None and len(base_date) > 10:
            raise ValueError("Invalid value for `base_date`, length must be less than or equal to `10`")  # noqa: E501
        if base_date is not None and len(base_date) < 10:
            raise ValueError("Invalid value for `base_date`, length must be greater than or equal to `10`")  # noqa: E501

        self._base_date = base_date

    @property
    def base_time(self):
        """Gets the base_time of this Account.  # noqa: E501

        基準時刻 半角文字 応答時刻、もしくは入金明細の基準時刻を示す。  ISO8601 時差(offset)も表記 HH:MM:SS+09:00形式   # noqa: E501

        :return: The base_time of this Account.  # noqa: E501
        :rtype: str
        """
        return self._base_time

    @base_time.setter
    def base_time(self, base_time):
        """Sets the base_time of this Account.

        基準時刻 半角文字 応答時刻、もしくは入金明細の基準時刻を示す。  ISO8601 時差(offset)も表記 HH:MM:SS+09:00形式   # noqa: E501

        :param base_time: The base_time of this Account.  # noqa: E501
        :type: str
        """
        if base_time is None:
            raise ValueError("Invalid value for `base_time`, must not be `None`")  # noqa: E501
        if base_time is not None and len(base_time) > 14:
            raise ValueError("Invalid value for `base_time`, length must be less than or equal to `14`")  # noqa: E501
        if base_time is not None and len(base_time) < 14:
            raise ValueError("Invalid value for `base_time`, length must be greater than or equal to `14`")  # noqa: E501

        self._base_time = base_time

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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
