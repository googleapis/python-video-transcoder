# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials   # type: ignore
from google.oauth2 import service_account              # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.video.transcoder_v1.services.transcoder_service import pagers
from google.cloud.video.transcoder_v1.types import resources
from google.cloud.video.transcoder_v1.types import services
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore
from .transports.base import TranscoderServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import TranscoderServiceGrpcAsyncIOTransport
from .client import TranscoderServiceClient


class TranscoderServiceAsyncClient:
    """Using the Transcoder API, you can queue asynchronous jobs for
    transcoding media into various output formats. Output formats
    may include different streaming standards such as HTTP Live
    Streaming (HLS) and Dynamic Adaptive Streaming over HTTP (DASH).
    You can also customize jobs using advanced features such as
    Digital Rights Management (DRM), audio equalization, content
    concatenation, and digital ad-stitch ready content generation.
    """

    _client: TranscoderServiceClient

    DEFAULT_ENDPOINT = TranscoderServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = TranscoderServiceClient.DEFAULT_MTLS_ENDPOINT

    job_path = staticmethod(TranscoderServiceClient.job_path)
    parse_job_path = staticmethod(TranscoderServiceClient.parse_job_path)
    job_template_path = staticmethod(TranscoderServiceClient.job_template_path)
    parse_job_template_path = staticmethod(TranscoderServiceClient.parse_job_template_path)
    common_billing_account_path = staticmethod(TranscoderServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(TranscoderServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(TranscoderServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(TranscoderServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(TranscoderServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(TranscoderServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(TranscoderServiceClient.common_project_path)
    parse_common_project_path = staticmethod(TranscoderServiceClient.parse_common_project_path)
    common_location_path = staticmethod(TranscoderServiceClient.common_location_path)
    parse_common_location_path = staticmethod(TranscoderServiceClient.parse_common_location_path)

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TranscoderServiceAsyncClient: The constructed client.
        """
        return TranscoderServiceClient.from_service_account_info.__func__(TranscoderServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TranscoderServiceAsyncClient: The constructed client.
        """
        return TranscoderServiceClient.from_service_account_file.__func__(TranscoderServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[ClientOptions] = None):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return TranscoderServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> TranscoderServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            TranscoderServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(type(TranscoderServiceClient).get_transport_class, type(TranscoderServiceClient))

    def __init__(self, *,
            credentials: ga_credentials.Credentials = None,
            transport: Union[str, TranscoderServiceTransport] = "grpc_asyncio",
            client_options: ClientOptions = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            ) -> None:
        """Instantiates the transcoder service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.TranscoderServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = TranscoderServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,

        )

    async def create_job(self,
            request: Union[services.CreateJobRequest, dict] = None,
            *,
            parent: str = None,
            job: resources.Job = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> resources.Job:
        r"""Creates a job in the specified region.

        .. code-block:: python

            from google.cloud.video import transcoder_v1

            def sample_create_job():
                # Create a client
                client = transcoder_v1.TranscoderServiceClient()

                # Initialize request argument(s)
                job = transcoder_v1.Job()
                job.template_id = "template_id_value"

                request = transcoder_v1.CreateJobRequest(
                    parent="parent_value",
                    job=job,
                )

                # Make the request
                response = client.create_job(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.video.transcoder_v1.types.CreateJobRequest, dict]):
                The request object. Request message for
                `TranscoderService.CreateJob`.
            parent (:class:`str`):
                Required. The parent location to create and process this
                job. Format: ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            job (:class:`google.cloud.video.transcoder_v1.types.Job`):
                Required. Parameters for creating
                transcoding job.

                This corresponds to the ``job`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.video.transcoder_v1.types.Job:
                Transcoding job resource.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, job])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = services.CreateJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if job is not None:
            request.job = job

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_job,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_jobs(self,
            request: Union[services.ListJobsRequest, dict] = None,
            *,
            parent: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListJobsAsyncPager:
        r"""Lists jobs in the specified region.

        .. code-block:: python

            from google.cloud.video import transcoder_v1

            def sample_list_jobs():
                # Create a client
                client = transcoder_v1.TranscoderServiceClient()

                # Initialize request argument(s)
                request = transcoder_v1.ListJobsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_jobs(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.video.transcoder_v1.types.ListJobsRequest, dict]):
                The request object. Request message for
                `TranscoderService.ListJobs`. The parent location from
                which to retrieve the collection of jobs.
            parent (:class:`str`):
                Required. Format:
                ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.video.transcoder_v1.services.transcoder_service.pagers.ListJobsAsyncPager:
                Response message for TranscoderService.ListJobs.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = services.ListJobsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_jobs,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListJobsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_job(self,
            request: Union[services.GetJobRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> resources.Job:
        r"""Returns the job data.

        .. code-block:: python

            from google.cloud.video import transcoder_v1

            def sample_get_job():
                # Create a client
                client = transcoder_v1.TranscoderServiceClient()

                # Initialize request argument(s)
                request = transcoder_v1.GetJobRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_job(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.video.transcoder_v1.types.GetJobRequest, dict]):
                The request object. Request message for
                `TranscoderService.GetJob`.
            name (:class:`str`):
                Required. The name of the job to retrieve. Format:
                ``projects/{project}/locations/{location}/jobs/{job}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.video.transcoder_v1.types.Job:
                Transcoding job resource.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = services.GetJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_job,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_job(self,
            request: Union[services.DeleteJobRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> None:
        r"""Deletes a job.

        .. code-block:: python

            from google.cloud.video import transcoder_v1

            def sample_delete_job():
                # Create a client
                client = transcoder_v1.TranscoderServiceClient()

                # Initialize request argument(s)
                request = transcoder_v1.DeleteJobRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_job(request=request)

        Args:
            request (Union[google.cloud.video.transcoder_v1.types.DeleteJobRequest, dict]):
                The request object. Request message for
                `TranscoderService.DeleteJob`.
            name (:class:`str`):
                Required. The name of the job to delete. Format:
                ``projects/{project}/locations/{location}/jobs/{job}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = services.DeleteJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_job,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def create_job_template(self,
            request: Union[services.CreateJobTemplateRequest, dict] = None,
            *,
            parent: str = None,
            job_template: resources.JobTemplate = None,
            job_template_id: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> resources.JobTemplate:
        r"""Creates a job template in the specified region.

        .. code-block:: python

            from google.cloud.video import transcoder_v1

            def sample_create_job_template():
                # Create a client
                client = transcoder_v1.TranscoderServiceClient()

                # Initialize request argument(s)
                request = transcoder_v1.CreateJobTemplateRequest(
                    parent="parent_value",
                    job_template_id="job_template_id_value",
                )

                # Make the request
                response = client.create_job_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.video.transcoder_v1.types.CreateJobTemplateRequest, dict]):
                The request object. Request message for
                `TranscoderService.CreateJobTemplate`.
            parent (:class:`str`):
                Required. The parent location to create this job
                template. Format:
                ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            job_template (:class:`google.cloud.video.transcoder_v1.types.JobTemplate`):
                Required. Parameters for creating job
                template.

                This corresponds to the ``job_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            job_template_id (:class:`str`):
                Required. The ID to use for the job template, which will
                become the final component of the job template's
                resource name.

                This value should be 4-63 characters, and valid
                characters must match the regular expression
                ``[a-zA-Z][a-zA-Z0-9_-]*``.

                This corresponds to the ``job_template_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.video.transcoder_v1.types.JobTemplate:
                Transcoding job template resource.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, job_template, job_template_id])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = services.CreateJobTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if job_template is not None:
            request.job_template = job_template
        if job_template_id is not None:
            request.job_template_id = job_template_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_job_template,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_job_templates(self,
            request: Union[services.ListJobTemplatesRequest, dict] = None,
            *,
            parent: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> pagers.ListJobTemplatesAsyncPager:
        r"""Lists job templates in the specified region.

        .. code-block:: python

            from google.cloud.video import transcoder_v1

            def sample_list_job_templates():
                # Create a client
                client = transcoder_v1.TranscoderServiceClient()

                # Initialize request argument(s)
                request = transcoder_v1.ListJobTemplatesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_job_templates(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.video.transcoder_v1.types.ListJobTemplatesRequest, dict]):
                The request object. Request message for
                `TranscoderService.ListJobTemplates`.
            parent (:class:`str`):
                Required. The parent location from which to retrieve the
                collection of job templates. Format:
                ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.video.transcoder_v1.services.transcoder_service.pagers.ListJobTemplatesAsyncPager:
                Response message for TranscoderService.ListJobTemplates.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = services.ListJobTemplatesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_job_templates,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("parent", request.parent),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListJobTemplatesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_job_template(self,
            request: Union[services.GetJobTemplateRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> resources.JobTemplate:
        r"""Returns the job template data.

        .. code-block:: python

            from google.cloud.video import transcoder_v1

            def sample_get_job_template():
                # Create a client
                client = transcoder_v1.TranscoderServiceClient()

                # Initialize request argument(s)
                request = transcoder_v1.GetJobTemplateRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_job_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.video.transcoder_v1.types.GetJobTemplateRequest, dict]):
                The request object. Request message for
                `TranscoderService.GetJobTemplate`.
            name (:class:`str`):
                Required. The name of the job template to retrieve.
                Format:
                ``projects/{project}/locations/{location}/jobTemplates/{job_template}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.video.transcoder_v1.types.JobTemplate:
                Transcoding job template resource.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = services.GetJobTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_job_template,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_job_template(self,
            request: Union[services.DeleteJobTemplateRequest, dict] = None,
            *,
            name: str = None,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: float = None,
            metadata: Sequence[Tuple[str, str]] = (),
            ) -> None:
        r"""Deletes a job template.

        .. code-block:: python

            from google.cloud.video import transcoder_v1

            def sample_delete_job_template():
                # Create a client
                client = transcoder_v1.TranscoderServiceClient()

                # Initialize request argument(s)
                request = transcoder_v1.DeleteJobTemplateRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_job_template(request=request)

        Args:
            request (Union[google.cloud.video.transcoder_v1.types.DeleteJobTemplateRequest, dict]):
                The request object. Request message for
                `TranscoderService.DeleteJobTemplate`.
            name (:class:`str`):
                Required. The name of the job template to delete.
                ``projects/{project}/locations/{location}/jobTemplates/{job_template}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError("If the `request` argument is set, then none of "
                             "the individual field arguments should be set.")

        request = services.DeleteJobTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_job_template,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((
                ("name", request.name),
            )),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-video-transcoder",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = (
    "TranscoderServiceAsyncClient",
)