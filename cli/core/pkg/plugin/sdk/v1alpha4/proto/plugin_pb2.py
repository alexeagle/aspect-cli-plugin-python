# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cli/core/pkg/plugin/sdk/v1alpha4/proto/plugin.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cli.core.bazel.buildeventstream import build_event_stream_pb2 as cli_dot_core_dot_bazel_dot_buildeventstream_dot_build__event__stream__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3cli/core/pkg/plugin/sdk/v1alpha4/proto/plugin.proto\x12\x05proto\x1a\x38\x63li/core/bazel/buildeventstream/build_event_stream.proto\"D\n\x13\x42\x45PEventCallbackReq\x12-\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1e.build_event_stream.BuildEvent\"\x15\n\x13\x42\x45PEventCallbackRes\"=\n\x08SetupReq\x12\x12\n\nproperties\x18\x01 \x01(\x0c\x12\x1d\n\x04\x66ile\x18\x02 \x01(\x0b\x32\x0b.proto.FileB\x02\x18\x01\"\x14\n\x04\x46ile\x12\x0c\n\x04path\x18\x01 \x01(\t\"\n\n\x08SetupRes\"B\n\x10PostBuildHookReq\x12\x11\n\tbroker_id\x18\x01 \x01(\r\x12\x1b\n\x13is_interactive_mode\x18\x02 \x01(\x08\"\x12\n\x10PostBuildHookRes\"=\n\x07\x43ommand\x12\x0b\n\x03use\x18\x01 \x01(\t\x12\x12\n\nshort_desc\x18\x02 \x01(\t\x12\x11\n\tlong_desc\x18\x03 \x01(\t\"\x13\n\x11\x43ustomCommandsReq\"5\n\x11\x43ustomCommandsRes\x12 \n\x08\x63ommands\x18\x01 \x03(\x0b\x32\x0e.proto.Command\" \n\x07\x43ontext\x12\x15\n\rworkspaceRoot\x18\x01 \x01(\t\"u\n\x17\x45xecuteCustomCommandReq\x12\x15\n\rcustomCommand\x18\x01 \x01(\t\x12\x1b\n\x03\x63tx\x18\x02 \x01(\x0b\x32\x0e.proto.Context\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x18\n\x10\x62\x61zelStartupArgs\x18\x04 \x03(\t\"\x19\n\x17\x45xecuteCustomCommandRes\"A\n\x0fPostTestHookReq\x12\x11\n\tbroker_id\x18\x01 \x01(\r\x12\x1b\n\x13is_interactive_mode\x18\x02 \x01(\x08\"\x11\n\x0fPostTestHookRes\"@\n\x0ePostRunHookReq\x12\x11\n\tbroker_id\x18\x01 \x01(\r\x12\x1b\n\x13is_interactive_mode\x18\x02 \x01(\x08\"\x10\n\x0ePostRunHookRes\"\x8f\x01\n\x0cPromptRunReq\x12\r\n\x05label\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\t\x12\x12\n\nallow_edit\x18\x03 \x01(\x08\x12\x0c\n\x04mask\x18\x05 \x01(\t\x12\x14\n\x0chide_entered\x18\x06 \x01(\x08\x12\x12\n\nis_confirm\x18\x08 \x01(\x08\x12\x13\n\x0bis_vim_mode\x18\t \x01(\x08\"t\n\x0cPromptRunRes\x12\x0e\n\x06result\x18\x01 \x01(\t\x12(\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x19.proto.PromptRunRes.Error\x1a*\n\x05\x45rror\x12\x10\n\x08happened\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xdd\x03\n\x06Plugin\x12J\n\x10\x42\x45PEventCallback\x12\x1a.proto.BEPEventCallbackReq\x1a\x1a.proto.BEPEventCallbackRes\x12\x44\n\x0e\x43ustomCommands\x12\x18.proto.CustomCommandsReq\x1a\x18.proto.CustomCommandsRes\x12V\n\x14\x45xecuteCustomCommand\x12\x1e.proto.ExecuteCustomCommandReq\x1a\x1e.proto.ExecuteCustomCommandRes\x12\x41\n\rPostBuildHook\x12\x17.proto.PostBuildHookReq\x1a\x17.proto.PostBuildHookRes\x12>\n\x0cPostTestHook\x12\x16.proto.PostTestHookReq\x1a\x16.proto.PostTestHookRes\x12;\n\x0bPostRunHook\x12\x15.proto.PostRunHookReq\x1a\x15.proto.PostRunHookRes\x12)\n\x05Setup\x12\x0f.proto.SetupReq\x1a\x0f.proto.SetupRes2;\n\x08Prompter\x12/\n\x03Run\x12\x13.proto.PromptRunReq\x1a\x13.proto.PromptRunResBEZCgithub.com/aspect-build/silo/cli/core/pkg/plugin/sdk/v1alpha4/protob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cli.core.pkg.plugin.sdk.v1alpha4.proto.plugin_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZCgithub.com/aspect-build/silo/cli/core/pkg/plugin/sdk/v1alpha4/proto'
  _SETUPREQ.fields_by_name['file']._options = None
  _SETUPREQ.fields_by_name['file']._serialized_options = b'\030\001'
  _BEPEVENTCALLBACKREQ._serialized_start=120
  _BEPEVENTCALLBACKREQ._serialized_end=188
  _BEPEVENTCALLBACKRES._serialized_start=190
  _BEPEVENTCALLBACKRES._serialized_end=211
  _SETUPREQ._serialized_start=213
  _SETUPREQ._serialized_end=274
  _FILE._serialized_start=276
  _FILE._serialized_end=296
  _SETUPRES._serialized_start=298
  _SETUPRES._serialized_end=308
  _POSTBUILDHOOKREQ._serialized_start=310
  _POSTBUILDHOOKREQ._serialized_end=376
  _POSTBUILDHOOKRES._serialized_start=378
  _POSTBUILDHOOKRES._serialized_end=396
  _COMMAND._serialized_start=398
  _COMMAND._serialized_end=459
  _CUSTOMCOMMANDSREQ._serialized_start=461
  _CUSTOMCOMMANDSREQ._serialized_end=480
  _CUSTOMCOMMANDSRES._serialized_start=482
  _CUSTOMCOMMANDSRES._serialized_end=535
  _CONTEXT._serialized_start=537
  _CONTEXT._serialized_end=569
  _EXECUTECUSTOMCOMMANDREQ._serialized_start=571
  _EXECUTECUSTOMCOMMANDREQ._serialized_end=688
  _EXECUTECUSTOMCOMMANDRES._serialized_start=690
  _EXECUTECUSTOMCOMMANDRES._serialized_end=715
  _POSTTESTHOOKREQ._serialized_start=717
  _POSTTESTHOOKREQ._serialized_end=782
  _POSTTESTHOOKRES._serialized_start=784
  _POSTTESTHOOKRES._serialized_end=801
  _POSTRUNHOOKREQ._serialized_start=803
  _POSTRUNHOOKREQ._serialized_end=867
  _POSTRUNHOOKRES._serialized_start=869
  _POSTRUNHOOKRES._serialized_end=885
  _PROMPTRUNREQ._serialized_start=888
  _PROMPTRUNREQ._serialized_end=1031
  _PROMPTRUNRES._serialized_start=1033
  _PROMPTRUNRES._serialized_end=1149
  _PROMPTRUNRES_ERROR._serialized_start=1107
  _PROMPTRUNRES_ERROR._serialized_end=1149
  _PLUGIN._serialized_start=1152
  _PLUGIN._serialized_end=1629
  _PROMPTER._serialized_start=1631
  _PROMPTER._serialized_end=1690
# @@protoc_insertion_point(module_scope)
