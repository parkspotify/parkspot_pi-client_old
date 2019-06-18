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


class NewUserRegistration(object):
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
        'name': 'str',
        'email': 'str',
        'password': 'str',
        'password_conf': 'str'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'password': 'password',
        'password_conf': 'password_conf'
    }

    def __init__(self, name=None, email=None, password=None, password_conf=None):  # noqa: E501
        """NewUserRegistration - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._email = None
        self._password = None
        self._password_conf = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if password is not None:
            self.password = password
        if password_conf is not None:
            self.password_conf = password_conf

    @property
    def name(self):
        """Gets the name of this NewUserRegistration.  # noqa: E501


        :return: The name of this NewUserRegistration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewUserRegistration.


        :param name: The name of this NewUserRegistration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this NewUserRegistration.  # noqa: E501


        :return: The email of this NewUserRegistration.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this NewUserRegistration.


        :param email: The email of this NewUserRegistration.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def password(self):
        """Gets the password of this NewUserRegistration.  # noqa: E501


        :return: The password of this NewUserRegistration.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this NewUserRegistration.


        :param password: The password of this NewUserRegistration.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def password_conf(self):
        """Gets the password_conf of this NewUserRegistration.  # noqa: E501


        :return: The password_conf of this NewUserRegistration.  # noqa: E501
        :rtype: str
        """
        return self._password_conf

    @password_conf.setter
    def password_conf(self, password_conf):
        """Sets the password_conf of this NewUserRegistration.


        :param password_conf: The password_conf of this NewUserRegistration.  # noqa: E501
        :type: str
        """

        self._password_conf = password_conf

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
        if issubclass(NewUserRegistration, dict):
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
        if not isinstance(other, NewUserRegistration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
