# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cli/core/bazel/options/option_filters.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+cli/core/bazel/options/option_filters.proto\x12\x07options*\xea\x02\n\x0fOptionEffectTag\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05NO_OP\x10\x01\x12\x1b\n\x17LOSES_INCREMENTAL_STATE\x10\x02\x12\x12\n\x0e\x43HANGES_INPUTS\x10\x03\x12\x13\n\x0f\x41\x46\x46\x45\x43TS_OUTPUTS\x10\x04\x12\x18\n\x14\x42UILD_FILE_SEMANTICS\x10\x05\x12 \n\x1c\x42\x41ZEL_INTERNAL_CONFIGURATION\x10\x06\x12\x18\n\x14LOADING_AND_ANALYSIS\x10\x07\x12\r\n\tEXECUTION\x10\x08\x12\'\n#HOST_MACHINE_RESOURCE_OPTIMIZATIONS\x10\t\x12\x15\n\x11\x45\x41GERNESS_TO_EXIT\x10\n\x12\x14\n\x10\x42\x41ZEL_MONITORING\x10\x0b\x12\x13\n\x0fTERMINAL_OUTPUT\x10\x0c\x12\x18\n\x14\x41\x43TION_COMMAND_LINES\x10\r\x12\x0f\n\x0bTEST_RUNNER\x10\x0e*\xc3\x01\n\x11OptionMetadataTag\x12\x10\n\x0c\x45XPERIMENTAL\x10\x00\x12\x17\n\x13INCOMPATIBLE_CHANGE\x10\x01\x12\x0e\n\nDEPRECATED\x10\x02\x12\n\n\x06HIDDEN\x10\x03\x12\x0c\n\x08INTERNAL\x10\x04\x12\r\n\tIMMUTABLE\x10\x07\"\x04\x08\x05\x10\x05\"\x04\x08\x06\x10\x06*%TRIGGERED_BY_ALL_INCOMPATIBLE_CHANGES*\x17\x45XPLICIT_IN_OUTPUT_PATHb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cli.core.bazel.options.option_filters_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_OPTIONEFFECTTAG']._serialized_start=57
  _globals['_OPTIONEFFECTTAG']._serialized_end=419
  _globals['_OPTIONMETADATATAG']._serialized_start=422
  _globals['_OPTIONMETADATATAG']._serialized_end=617
# @@protoc_insertion_point(module_scope)
