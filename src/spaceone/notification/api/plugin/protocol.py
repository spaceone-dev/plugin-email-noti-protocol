from spaceone.api.notification.plugin import protocol_pb2_grpc, protocol_pb2
from spaceone.core.pygrpc import BaseAPI


class Protocol(BaseAPI, protocol_pb2_grpc.ProtocolServicer):
    pb2 = protocol_pb2
    pb2_grpc = protocol_pb2_grpc

    def init(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('ProtocolService', metadata) as protocol_svc:
            plugin_info = protocol_svc.init(params)
            return self.locator.get_info('PluginInfo', plugin_info)

    def verify(self, request, context):
        params, metadata = self.parse_request(request, context)

        with self.locator.get_service('ProtocolService', metadata) as protocol_svc:
            protocol_svc.verify(params)
            return self.locator.get_info('EmptyInfo')
