#!/usr/bin/env python3
from concurrent import futures
import sys
import time

import grpc

from proto import aspect_plugin_pb2
from proto import aspect_plugin_pb2_grpc

from grpc_health.v1.health import HealthServicer
from grpc_health.v1 import health_pb2, health_pb2_grpc

class PluginServicer(aspect_plugin_pb2_grpc.PluginServicer):
    """Implementation of Plugin service."""

    def PostBuildHook(self, request, context):
        return aspect_plugin_pb2.PostBuildHookRes()
    def PostTestHook(self, request, context):
        return aspect_plugin_pb2.PostTestHookRes()
    def PostRunHook(self, request, context):
        return aspect_plugin_pb2.PostRunHookRes()
    def BEPEventCallback(self, request, context):
        return aspect_plugin_pb2.BEPEventCallbackRes()
    def CustomCommands(self, request, context):
        res = aspect_plugin_pb2.CustomCommandsRes()
        com = aspect_plugin_pb2.Command()
        com.use = "custom_from_python"
        com.short_desc = "custom command written in python"
        com.long_desc = ""
        res.commands.append(com)
        return res
    def ExecuteCustomCommand(self, request, context):
        return aspect_plugin_pb2.ExecuteCustomCommandRes()
    def Setup(self, request, context):
        return aspect_plugin_pb2.SetupRes()

def serve():
    # We need to build a health service to work with go-plugin
    health = HealthServicer()
    health.set("plugin", health_pb2.HealthCheckResponse.ServingStatus.Value('SERVING'))

    # Start the server.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    aspect_plugin_pb2_grpc.add_PluginServicer_to_server(PluginServicer(), server)
    health_pb2_grpc.add_HealthServicer_to_server(health, server)
    server.add_insecure_port('127.0.0.1:1234')
    server.start()

    # Output information
    print("1|3|tcp|127.0.0.1:1234|grpc")
    sys.stdout.flush()

    server.wait_for_termination()

if __name__ == '__main__':
    serve()
