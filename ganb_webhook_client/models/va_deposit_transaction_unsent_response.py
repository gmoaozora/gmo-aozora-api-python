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

from ganb_webhook_client.models.va_deposit_transaction_message import VaDepositTransactionMessage  # noqa: F401,E501


class VaDepositTransactionUnsentResponse(object):
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
        'messages': 'list[VaDepositTransactionMessage]'
    }

    attribute_map = {
        'messages': 'messages'
    }

    def __init__(self, messages=None):  # noqa: E501
        """VaDepositTransactionUnsentResponse - a model defined in Swagger"""  # noqa: E501

        self._messages = None
        self.discriminator = None

        self.messages = messages

    @property
    def messages(self):
        """Gets the messages of this VaDepositTransactionUnsentResponse.  # noqa: E501


        :return: The messages of this VaDepositTransactionUnsentResponse.  # noqa: E501
        :rtype: list[VaDepositTransactionMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this VaDepositTransactionUnsentResponse.


        :param messages: The messages of this VaDepositTransactionUnsentResponse.  # noqa: E501
        :type: list[VaDepositTransactionMessage]
        """
        if messages is None:
            raise ValueError("Invalid value for `messages`, must not be `None`")  # noqa: E501

        self._messages = messages

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
        if issubclass(VaDepositTransactionUnsentResponse, dict):
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
        if not isinstance(other, VaDepositTransactionUnsentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
