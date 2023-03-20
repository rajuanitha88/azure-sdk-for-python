# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AlertSeverity(int, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Severity of the alert. Should be an integer between [0-4]. Value of 0 is severest. Relevant and
    required only for rules of the kind LogAlert.
    """

    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4


class ConditionOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The criteria operator. Relevant and required only for rules of the kind LogAlert."""

    EQUALS = "Equals"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DimensionOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operator for dimension values."""

    INCLUDE = "Include"
    EXCLUDE = "Exclude"


class IdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of managed service identity."""

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    NONE = "None"


class Kind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the type of scheduled query rule. The default is LogAlert."""

    LOG_ALERT = "LogAlert"
    LOG_TO_METRIC = "LogToMetric"


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This determines if traffic is allowed over public network. By default it is enabled."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"
    SECURED_BY_PERIMETER = "SecuredByPerimeter"


class TimeAggregation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Aggregation type. Relevant and required only for rules of the kind LogAlert."""

    COUNT = "Count"
    AVERAGE = "Average"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    TOTAL = "Total"
