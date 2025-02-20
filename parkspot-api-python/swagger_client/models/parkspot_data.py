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


class ParkspotData(object):
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
        'id': 'str',
        'name': 'str',
        'total_places_count': 'int',
        'occupied_places_count': 'int',
        'local_ip': 'str',
        'token': 'str',
        'is_setup': 'bool'
    }

    attribute_map = {
        'id': '_id',
        'name': 'name',
        'total_places_count': 'total_places_count',
        'occupied_places_count': 'occupied_places_count',
        'local_ip': 'local_ip',
        'token': 'token',
        'is_setup': 'is_setup'
    }

    def __init__(self, id=None, name=None, total_places_count=None, occupied_places_count=None, local_ip=None, token=None, is_setup=None):  # noqa: E501
        """ParkspotData - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._total_places_count = None
        self._occupied_places_count = None
        self._local_ip = None
        self._token = None
        self._is_setup = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if total_places_count is not None:
            self.total_places_count = total_places_count
        if occupied_places_count is not None:
            self.occupied_places_count = occupied_places_count
        if local_ip is not None:
            self.local_ip = local_ip
        if token is not None:
            self.token = token
        if is_setup is not None:
            self.is_setup = is_setup

    @property
    def id(self):
        """Gets the id of this ParkspotData.  # noqa: E501


        :return: The id of this ParkspotData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ParkspotData.


        :param id: The id of this ParkspotData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ParkspotData.  # noqa: E501


        :return: The name of this ParkspotData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParkspotData.


        :param name: The name of this ParkspotData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def total_places_count(self):
        """Gets the total_places_count of this ParkspotData.  # noqa: E501


        :return: The total_places_count of this ParkspotData.  # noqa: E501
        :rtype: int
        """
        return self._total_places_count

    @total_places_count.setter
    def total_places_count(self, total_places_count):
        """Sets the total_places_count of this ParkspotData.


        :param total_places_count: The total_places_count of this ParkspotData.  # noqa: E501
        :type: int
        """

        self._total_places_count = total_places_count

    @property
    def occupied_places_count(self):
        """Gets the occupied_places_count of this ParkspotData.  # noqa: E501


        :return: The occupied_places_count of this ParkspotData.  # noqa: E501
        :rtype: int
        """
        return self._occupied_places_count

    @occupied_places_count.setter
    def occupied_places_count(self, occupied_places_count):
        """Sets the occupied_places_count of this ParkspotData.


        :param occupied_places_count: The occupied_places_count of this ParkspotData.  # noqa: E501
        :type: int
        """

        self._occupied_places_count = occupied_places_count

    @property
    def local_ip(self):
        """Gets the local_ip of this ParkspotData.  # noqa: E501


        :return: The local_ip of this ParkspotData.  # noqa: E501
        :rtype: str
        """
        return self._local_ip

    @local_ip.setter
    def local_ip(self, local_ip):
        """Sets the local_ip of this ParkspotData.


        :param local_ip: The local_ip of this ParkspotData.  # noqa: E501
        :type: str
        """

        self._local_ip = local_ip

    @property
    def token(self):
        """Gets the token of this ParkspotData.  # noqa: E501


        :return: The token of this ParkspotData.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ParkspotData.


        :param token: The token of this ParkspotData.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def is_setup(self):
        """Gets the is_setup of this ParkspotData.  # noqa: E501


        :return: The is_setup of this ParkspotData.  # noqa: E501
        :rtype: bool
        """
        return self._is_setup

    @is_setup.setter
    def is_setup(self, is_setup):
        """Sets the is_setup of this ParkspotData.


        :param is_setup: The is_setup of this ParkspotData.  # noqa: E501
        :type: bool
        """

        self._is_setup = is_setup

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
        if issubclass(ParkspotData, dict):
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
        if not isinstance(other, ParkspotData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
