# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import map_error

from ... import models


class ServiceOperations:
    """ServiceOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar restype: . Constant value: "service".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config
        self.restype = "service"

    async def set_properties(self, storage_service_properties, timeout=None, request_id=None, *, cls=None, **kwargs):
        """Sets properties for a storage account's Queue service endpoint,
        including properties for Storage Analytics and CORS (Cross-Origin
        Resource Sharing) rules.

        :param storage_service_properties: The StorageService properties.
        :type storage_service_properties:
         ~azure.storage.queue.models.StorageServiceProperties
        :param timeout: The The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>
        :type timeout: int
        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<azure.storage.queue.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "properties"

        # Construct URL
        url = self.set_properties.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')

        # Construct body
        body_content = self._serialize.body(storage_service_properties, 'StorageServiceProperties')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    set_properties.metadata = {'url': '/'}

    async def get_properties(self, timeout=None, request_id=None, *, cls=None, **kwargs):
        """gets the properties of a storage account's Queue service, including
        properties for Storage Analytics and CORS (Cross-Origin Resource
        Sharing) rules.

        :param timeout: The The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>
        :type timeout: int
        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: StorageServiceProperties or the result of cls(response)
        :rtype: ~azure.storage.queue.models.StorageServiceProperties
        :raises:
         :class:`StorageErrorException<azure.storage.queue.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "properties"

        # Construct URL
        url = self.get_properties.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('StorageServiceProperties', response)
            header_dict = {
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }

        if cls:
            return cls(response, deserialized, header_dict)

        return deserialized
    get_properties.metadata = {'url': '/'}

    async def get_statistics(self, timeout=None, request_id=None, *, cls=None, **kwargs):
        """Retrieves statistics related to replication for the Queue service. It
        is only available on the secondary location endpoint when read-access
        geo-redundant replication is enabled for the storage account.

        :param timeout: The The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>
        :type timeout: int
        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: StorageServiceStats or the result of cls(response)
        :rtype: ~azure.storage.queue.models.StorageServiceStats
        :raises:
         :class:`StorageErrorException<azure.storage.queue.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "stats"

        # Construct URL
        url = self.get_statistics.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('StorageServiceStats', response)
            header_dict = {
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }

        if cls:
            return cls(response, deserialized, header_dict)

        return deserialized
    get_statistics.metadata = {'url': '/'}

    async def list_queues_segment(self, prefix=None, marker=None, maxresults=None, include=None, timeout=None, request_id=None, *, cls=None, **kwargs):
        """The List Queues Segment operation returns a list of the queues under
        the specified account.

        :param prefix: Filters the results to return only queues whose name
         begins with the specified prefix.
        :type prefix: str
        :param marker: A string value that identifies the portion of the list
         of queues to be returned with the next listing operation. The
         operation returns the NextMarker value within the response body if the
         listing operation did not return all queues remaining to be listed
         with the current page. The NextMarker value can be used as the value
         for the marker parameter in a subsequent call to request the next page
         of list items. The marker value is opaque to the client.
        :type marker: str
        :param maxresults: Specifies the maximum number of queues to return.
         If the request does not specify maxresults, or specifies a value
         greater than 5000, the server will return up to 5000 items. Note that
         if the listing operation crosses a partition boundary, then the
         service will return a continuation token for retrieving the remainder
         of the results. For this reason, it is possible that the service will
         return fewer results than specified by maxresults, or than the default
         of 5000.
        :type maxresults: int
        :param include: Include this parameter to specify that the queues's
         metadata be returned as part of the response body.
        :type include: list[str or
         ~azure.storage.queue.models.ListQueuesIncludeType]
        :param timeout: The The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/setting-timeouts-for-queue-service-operations>Setting
         Timeouts for Queue Service Operations.</a>
        :type timeout: int
        :param request_id: Provides a client-generated, opaque value with a 1
         KB character limit that is recorded in the analytics logs when storage
         analytics logging is enabled.
        :type request_id: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: ListQueuesSegmentResponse or the result of cls(response)
        :rtype: ~azure.storage.queue.models.ListQueuesSegmentResponse
        :raises:
         :class:`StorageErrorException<azure.storage.queue.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "list"

        # Construct URL
        url = self.list_queues_segment.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if prefix is not None:
            query_parameters['prefix'] = self._serialize.query("prefix", prefix, 'str')
        if marker is not None:
            query_parameters['marker'] = self._serialize.query("marker", marker, 'str')
        if maxresults is not None:
            query_parameters['maxresults'] = self._serialize.query("maxresults", maxresults, 'int', minimum=1)
        if include is not None:
            query_parameters['include'] = self._serialize.query("include", include, '[ListQueuesIncludeType]', div=',')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id", request_id, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ListQueuesSegmentResponse', response)
            header_dict = {
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }

        if cls:
            return cls(response, deserialized, header_dict)

        return deserialized
    list_queues_segment.metadata = {'url': '/'}
