# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cli/core/bazel/invocation_policy/invocation_policy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8cli/core/bazel/invocation_policy/invocation_policy.proto\x12\x17\x62laze.invocation_policy\"\\\n\x10InvocationPolicy\x12H\n\rflag_policies\x18\x01 \x03(\x0b\x32#.blaze.invocation_policy.FlagPolicyR\x0c\x66lagPolicies\"\xfb\x02\n\nFlagPolicy\x12\x1b\n\tflag_name\x18\x01 \x01(\tR\x08\x66lagName\x12\x1a\n\x08\x63ommands\x18\x02 \x03(\tR\x08\x63ommands\x12@\n\tset_value\x18\x03 \x01(\x0b\x32!.blaze.invocation_policy.SetValueH\x00R\x08setValue\x12\x46\n\x0buse_default\x18\x04 \x01(\x0b\x32#.blaze.invocation_policy.UseDefaultH\x00R\nuseDefault\x12R\n\x0f\x64isallow_values\x18\x05 \x01(\x0b\x32\'.blaze.invocation_policy.DisallowValuesH\x00R\x0e\x64isallowValues\x12I\n\x0c\x61llow_values\x18\x06 \x01(\x0b\x32$.blaze.invocation_policy.AllowValuesH\x00R\x0b\x61llowValuesB\x0b\n\toperation\"\xdb\x01\n\x08SetValue\x12\x1d\n\nflag_value\x18\x01 \x03(\tR\tflagValue\x12\x46\n\x08\x62\x65havior\x18\x04 \x01(\x0e\x32*.blaze.invocation_policy.SetValue.BehaviorR\x08\x62\x65havior\"\\\n\x08\x42\x65havior\x12\r\n\tUNDEFINED\x10\x00\x12\x13\n\x0f\x41LLOW_OVERRIDES\x10\x01\x12\n\n\x06\x41PPEND\x10\x02\x12 \n\x1c\x46INAL_VALUE_IGNORE_OVERRIDES\x10\x03J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04\"\x0c\n\nUseDefault\"\xbf\x01\n\x0e\x44isallowValues\x12+\n\x11\x64isallowed_values\x18\x01 \x03(\tR\x10\x64isallowedValues\x12\x1d\n\tnew_value\x18\x03 \x01(\tH\x00R\x08newValue\x12\x46\n\x0buse_default\x18\x04 \x01(\x0b\x32#.blaze.invocation_policy.UseDefaultH\x00R\nuseDefaultB\x13\n\x11replacement_valueJ\x04\x08\x02\x10\x03\"\xb6\x01\n\x0b\x41llowValues\x12%\n\x0e\x61llowed_values\x18\x01 \x03(\tR\rallowedValues\x12\x1d\n\tnew_value\x18\x03 \x01(\tH\x00R\x08newValue\x12\x46\n\x0buse_default\x18\x04 \x01(\x0b\x32#.blaze.invocation_policy.UseDefaultH\x00R\nuseDefaultB\x13\n\x11replacement_valueJ\x04\x08\x02\x10\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cli.core.bazel.invocation_policy.invocation_policy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_INVOCATIONPOLICY']._serialized_start=85
  _globals['_INVOCATIONPOLICY']._serialized_end=177
  _globals['_FLAGPOLICY']._serialized_start=180
  _globals['_FLAGPOLICY']._serialized_end=559
  _globals['_SETVALUE']._serialized_start=562
  _globals['_SETVALUE']._serialized_end=781
  _globals['_SETVALUE_BEHAVIOR']._serialized_start=677
  _globals['_SETVALUE_BEHAVIOR']._serialized_end=769
  _globals['_USEDEFAULT']._serialized_start=783
  _globals['_USEDEFAULT']._serialized_end=795
  _globals['_DISALLOWVALUES']._serialized_start=798
  _globals['_DISALLOWVALUES']._serialized_end=989
  _globals['_ALLOWVALUES']._serialized_start=992
  _globals['_ALLOWVALUES']._serialized_end=1174
# @@protoc_insertion_point(module_scope)
