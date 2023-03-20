# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
import sys
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar, Union
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    resource_uri: str,
    *,
    metricnames: Optional[str] = None,
    metricnamespace: Optional[str] = None,
    timespan: Optional[str] = None,
    interval: Optional[datetime.timedelta] = None,
    aggregation: Optional[str] = None,
    sensitivities: Optional[str] = None,
    filter: Optional[str] = None,
    result_type: Optional[Union[str, _models.ResultType]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2019-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2019-03-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{resourceUri}/providers/Microsoft.Insights/metricBaselines")
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    if metricnames is not None:
        _params["metricnames"] = _SERIALIZER.query("metricnames", metricnames, "str")
    if metricnamespace is not None:
        _params["metricnamespace"] = _SERIALIZER.query("metricnamespace", metricnamespace, "str")
    if timespan is not None:
        _params["timespan"] = _SERIALIZER.query("timespan", timespan, "str")
    if interval is not None:
        _params["interval"] = _SERIALIZER.query("interval", interval, "duration")
    if aggregation is not None:
        _params["aggregation"] = _SERIALIZER.query("aggregation", aggregation, "str")
    if sensitivities is not None:
        _params["sensitivities"] = _SERIALIZER.query("sensitivities", sensitivities, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if result_type is not None:
        _params["resultType"] = _SERIALIZER.query("result_type", result_type, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class BaselinesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~$(python-base-namespace).v2019_03_01.MonitorManagementClient`'s
        :attr:`baselines` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self,
        resource_uri: str,
        metricnames: Optional[str] = None,
        metricnamespace: Optional[str] = None,
        timespan: Optional[str] = None,
        interval: Optional[datetime.timedelta] = None,
        aggregation: Optional[str] = None,
        sensitivities: Optional[str] = None,
        filter: Optional[str] = None,
        result_type: Optional[Union[str, _models.ResultType]] = None,
        **kwargs: Any
    ) -> Iterable["_models.SingleMetricBaseline"]:
        """**Lists the metric baseline values for a resource**.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param metricnames: The names of the metrics (comma separated) to retrieve. Special case: If a
         metricname itself has a comma in it then use %2 to indicate it. Eg: 'Metric,Name1' should be
         **'Metric%2Name1'**. Default value is None.
        :type metricnames: str
        :param metricnamespace: Metric namespace to query metric definitions for. Default value is
         None.
        :type metricnamespace: str
        :param timespan: The timespan of the query. It is a string with the following format
         'startDateTime_ISO/endDateTime_ISO'. Default value is None.
        :type timespan: str
        :param interval: The interval (i.e. timegrain) of the query. Default value is None.
        :type interval: ~datetime.timedelta
        :param aggregation: The list of aggregation types (comma separated) to retrieve. Default value
         is None.
        :type aggregation: str
        :param sensitivities: The list of sensitivities (comma separated) to retrieve. Default value is
         None.
        :type sensitivities: str
        :param filter: The **$filter** is used to reduce the set of metric data returned. Example:
         Metric contains metadata A, B and C. - Return all time series of C where A = a1 and B = b1 or
         b2 **$filter=A eq 'a1' and B eq 'b1' or B eq 'b2' and C eq '*'** - Invalid variant: **$filter=A
         eq 'a1' and B eq 'b1' and C eq '*' or B = 'b2'** This is invalid because the logical or
         operator cannot separate two different metadata names. - Return all time series where A = a1, B
         = b1 and C = c1: **$filter=A eq 'a1' and B eq 'b1' and C eq 'c1'** - Return all time series
         where A = a1 **$filter=A eq 'a1' and B eq '\ *' and C eq '*\ '**. Special case: When dimension
         name or dimension value uses round brackets. Eg: When dimension name is **dim (test) 1**
         Instead of using $filter= "dim (test) 1 eq '\ *' " use **$filter= "dim %2528test%2529 1 eq '*\
         ' "\ ** When dimension name is **\ dim (test) 3\ ** and dimension value is **\ dim3 (test) val\
         ** Instead of using $filter= "dim (test) 3 eq 'dim3 (test) val' " use **\ $filter= "dim
         %2528test%2529 3 eq 'dim3 %2528test%2529 val' "**. Default value is None.
        :type filter: str
        :param result_type: Allows retrieving only metadata of the baseline. On data request all
         information is retrieved. Known values are: "Data" and "Metadata". Default value is None.
        :type result_type: str or ~$(python-base-namespace).v2019_03_01.models.ResultType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SingleMetricBaseline or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~$(python-base-namespace).v2019_03_01.models.SingleMetricBaseline]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2019-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2019-03-01"))
        cls: ClsType[_models.MetricBaselinesResponse] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_uri=resource_uri,
                    metricnames=metricnames,
                    metricnamespace=metricnamespace,
                    timespan=timespan,
                    interval=interval,
                    aggregation=aggregation,
                    sensitivities=sensitivities,
                    filter=filter,
                    result_type=result_type,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("MetricBaselinesResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {"url": "/{resourceUri}/providers/Microsoft.Insights/metricBaselines"}
