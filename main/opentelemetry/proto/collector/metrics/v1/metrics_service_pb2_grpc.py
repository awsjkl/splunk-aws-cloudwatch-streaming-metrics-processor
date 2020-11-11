# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from opentelemetry.proto.collector.metrics.v1 import \
	metrics_service_pb2 as opentelemetry_dot_proto_dot_collector_dot_metrics_dot_v1_dot_metrics__service__pb2


class MetricsServiceStub(object):
    """Service that can be used to push metrics between one Application
    instrumented with OpenTelemetry and a collector, or between a collector and a
    central collector.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Export = channel.unary_unary(
                '/opentelemetry.proto.collector.metrics.v1.MetricsService/Export',
                request_serializer=opentelemetry_dot_proto_dot_collector_dot_metrics_dot_v1_dot_metrics__service__pb2.ExportMetricsServiceRequest.SerializeToString,
                response_deserializer=opentelemetry_dot_proto_dot_collector_dot_metrics_dot_v1_dot_metrics__service__pb2.ExportMetricsServiceResponse.FromString,
                )


class MetricsServiceServicer(object):
    """Service that can be used to push metrics between one Application
    instrumented with OpenTelemetry and a collector, or between a collector and a
    central collector.
    """

    def Export(self, request, context):
        """For performance reasons, it is recommended to keep this RPC
        alive for the entire life of the application.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MetricsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Export': grpc.unary_unary_rpc_method_handler(
                    servicer.Export,
                    request_deserializer=opentelemetry_dot_proto_dot_collector_dot_metrics_dot_v1_dot_metrics__service__pb2.ExportMetricsServiceRequest.FromString,
                    response_serializer=opentelemetry_dot_proto_dot_collector_dot_metrics_dot_v1_dot_metrics__service__pb2.ExportMetricsServiceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'opentelemetry.proto.collector.metrics.v1.MetricsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MetricsService(object):
    """Service that can be used to push metrics between one Application
    instrumented with OpenTelemetry and a collector, or between a collector and a
    central collector.
    """

    @staticmethod
    def Export(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/opentelemetry.proto.collector.metrics.v1.MetricsService/Export',
            opentelemetry_dot_proto_dot_collector_dot_metrics_dot_v1_dot_metrics__service__pb2.ExportMetricsServiceRequest.SerializeToString,
            opentelemetry_dot_proto_dot_collector_dot_metrics_dot_v1_dot_metrics__service__pb2.ExportMetricsServiceResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
