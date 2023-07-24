# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import CustomCertificate
from ._models_py3 import CustomCertificateList
from ._models_py3 import CustomDomain
from ._models_py3 import CustomDomainList
from ._models_py3 import Dimension
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import EventHandler
from ._models_py3 import EventHubEndpoint
from ._models_py3 import EventListener
from ._models_py3 import EventListenerEndpoint
from ._models_py3 import EventListenerFilter
from ._models_py3 import EventNameFilter
from ._models_py3 import LiveTraceCategory
from ._models_py3 import LiveTraceConfiguration
from ._models_py3 import LogSpecification
from ._models_py3 import ManagedIdentity
from ._models_py3 import ManagedIdentitySettings
from ._models_py3 import MetricSpecification
from ._models_py3 import NameAvailability
from ._models_py3 import NameAvailabilityParameters
from ._models_py3 import NetworkACL
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationList
from ._models_py3 import OperationProperties
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointACL
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionList
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceList
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import ProxyResource
from ._models_py3 import RegenerateKeyParameters
from ._models_py3 import Replica
from ._models_py3 import ReplicaList
from ._models_py3 import Resource
from ._models_py3 import ResourceLogCategory
from ._models_py3 import ResourceLogConfiguration
from ._models_py3 import ResourceReference
from ._models_py3 import ResourceSku
from ._models_py3 import ServiceSpecification
from ._models_py3 import ShareablePrivateLinkResourceProperties
from ._models_py3 import ShareablePrivateLinkResourceType
from ._models_py3 import SharedPrivateLinkResource
from ._models_py3 import SharedPrivateLinkResourceList
from ._models_py3 import SignalRServiceUsage
from ._models_py3 import SignalRServiceUsageList
from ._models_py3 import SignalRServiceUsageName
from ._models_py3 import Sku
from ._models_py3 import SkuCapacity
from ._models_py3 import SkuList
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import UpstreamAuthSettings
from ._models_py3 import UserAssignedIdentityProperty
from ._models_py3 import WebPubSubHub
from ._models_py3 import WebPubSubHubList
from ._models_py3 import WebPubSubHubProperties
from ._models_py3 import WebPubSubKeys
from ._models_py3 import WebPubSubNetworkACLs
from ._models_py3 import WebPubSubResource
from ._models_py3 import WebPubSubResourceList
from ._models_py3 import WebPubSubTlsSettings

from ._web_pub_sub_management_client_enums import ACLAction
from ._web_pub_sub_management_client_enums import CreatedByType
from ._web_pub_sub_management_client_enums import EventListenerEndpointDiscriminator
from ._web_pub_sub_management_client_enums import EventListenerFilterDiscriminator
from ._web_pub_sub_management_client_enums import KeyType
from ._web_pub_sub_management_client_enums import ManagedIdentityType
from ._web_pub_sub_management_client_enums import PrivateLinkServiceConnectionStatus
from ._web_pub_sub_management_client_enums import ProvisioningState
from ._web_pub_sub_management_client_enums import ScaleType
from ._web_pub_sub_management_client_enums import ServiceKind
from ._web_pub_sub_management_client_enums import SharedPrivateLinkResourceStatus
from ._web_pub_sub_management_client_enums import UpstreamAuthType
from ._web_pub_sub_management_client_enums import WebPubSubRequestType
from ._web_pub_sub_management_client_enums import WebPubSubSkuTier
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CustomCertificate",
    "CustomCertificateList",
    "CustomDomain",
    "CustomDomainList",
    "Dimension",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "EventHandler",
    "EventHubEndpoint",
    "EventListener",
    "EventListenerEndpoint",
    "EventListenerFilter",
    "EventNameFilter",
    "LiveTraceCategory",
    "LiveTraceConfiguration",
    "LogSpecification",
    "ManagedIdentity",
    "ManagedIdentitySettings",
    "MetricSpecification",
    "NameAvailability",
    "NameAvailabilityParameters",
    "NetworkACL",
    "Operation",
    "OperationDisplay",
    "OperationList",
    "OperationProperties",
    "PrivateEndpoint",
    "PrivateEndpointACL",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionList",
    "PrivateLinkResource",
    "PrivateLinkResourceList",
    "PrivateLinkServiceConnectionState",
    "ProxyResource",
    "RegenerateKeyParameters",
    "Replica",
    "ReplicaList",
    "Resource",
    "ResourceLogCategory",
    "ResourceLogConfiguration",
    "ResourceReference",
    "ResourceSku",
    "ServiceSpecification",
    "ShareablePrivateLinkResourceProperties",
    "ShareablePrivateLinkResourceType",
    "SharedPrivateLinkResource",
    "SharedPrivateLinkResourceList",
    "SignalRServiceUsage",
    "SignalRServiceUsageList",
    "SignalRServiceUsageName",
    "Sku",
    "SkuCapacity",
    "SkuList",
    "SystemData",
    "TrackedResource",
    "UpstreamAuthSettings",
    "UserAssignedIdentityProperty",
    "WebPubSubHub",
    "WebPubSubHubList",
    "WebPubSubHubProperties",
    "WebPubSubKeys",
    "WebPubSubNetworkACLs",
    "WebPubSubResource",
    "WebPubSubResourceList",
    "WebPubSubTlsSettings",
    "ACLAction",
    "CreatedByType",
    "EventListenerEndpointDiscriminator",
    "EventListenerFilterDiscriminator",
    "KeyType",
    "ManagedIdentityType",
    "PrivateLinkServiceConnectionStatus",
    "ProvisioningState",
    "ScaleType",
    "ServiceKind",
    "SharedPrivateLinkResourceStatus",
    "UpstreamAuthType",
    "WebPubSubRequestType",
    "WebPubSubSkuTier",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
