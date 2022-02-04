# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import crawler_pb2 as crawler__pb2


class CrawlerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.start = channel.unary_unary(
                '/Crawler/start',
                request_serializer=crawler__pb2.Request.SerializeToString,
                response_deserializer=crawler__pb2.Reply.FromString,
                )
        self.stop = channel.unary_unary(
                '/Crawler/stop',
                request_serializer=crawler__pb2.Request.SerializeToString,
                response_deserializer=crawler__pb2.Reply.FromString,
                )
        self.list = channel.unary_unary(
                '/Crawler/list',
                request_serializer=crawler__pb2.Request.SerializeToString,
                response_deserializer=crawler__pb2.Reply.FromString,
                )


class CrawlerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def start(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stop(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CrawlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'start': grpc.unary_unary_rpc_method_handler(
                    servicer.start,
                    request_deserializer=crawler__pb2.Request.FromString,
                    response_serializer=crawler__pb2.Reply.SerializeToString,
            ),
            'stop': grpc.unary_unary_rpc_method_handler(
                    servicer.stop,
                    request_deserializer=crawler__pb2.Request.FromString,
                    response_serializer=crawler__pb2.Reply.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=crawler__pb2.Request.FromString,
                    response_serializer=crawler__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Crawler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Crawler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Crawler/start',
            crawler__pb2.Request.SerializeToString,
            crawler__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Crawler/stop',
            crawler__pb2.Request.SerializeToString,
            crawler__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Crawler/list',
            crawler__pb2.Request.SerializeToString,
            crawler__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
