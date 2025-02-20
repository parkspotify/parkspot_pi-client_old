# coding: utf-8

"""
    Swagger Parkspot2.0

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: test@test.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.inline_response2003_error import InlineResponse2003Error  # noqa: F401,E501


class InlineResponse201(object):
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
        'success': 'bool',
        'error': 'InlineResponse2003Error',
        'parkspot_id': 'str'
    }

    attribute_map = {
        'success': 'success',
        'error': 'error',
        'parkspot_id': 'parkspotID'
    }

    def __init__(self, success=None, error=None, parkspot_id=None):  # noqa: E501
        """InlineResponse201 - a model defined in Swagger"""  # noqa: E501

        self._success = None
        self._error = None
        self._parkspot_id = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if error is not None:
            self.error = error
        if parkspot_id is not None:
            self.parkspot_id = parkspot_id

    @property
    def success(self):
        """Gets the success of this InlineResponse201.  # noqa: E501


        :return: The success of this InlineResponse201.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse201.


        :param success: The success of this InlineResponse201.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def error(self):
        """Gets the error of this InlineResponse201.  # noqa: E501


        :return: The error of this InlineResponse201.  # noqa: E501
        :rtype: InlineResponse2003Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this InlineResponse201.


        :param error: The error of this InlineResponse201.  # noqa: E501
        :type: InlineResponse2003Error
        """

        self._error = error

    @property
    def parkspot_id(self):
        """Gets the parkspot_id of this InlineResponse201.  # noqa: E501


        :return: The parkspot_id of this InlineResponse201.  # noqa: E501
        :rtype: str
        """
        return self._parkspot_id

    @parkspot_id.setter
    def parkspot_id(self, parkspot_id):
        """Sets the parkspot_id of this InlineResponse201.


        :param parkspot_id: The parkspot_id of this InlineResponse201.  # noqa: E501
        :type: str
        """

        self._parkspot_id = parkspot_id

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
        if issubclass(InlineResponse201, dict):
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
        if not isinstance(other, InlineResponse201):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
