# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: activityPredictor.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'activityPredictor.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61\x63tivityPredictor.proto\x12\x11\x61\x63tivityPredictor\"(\n\nAddRequest\x12\x0c\n\x04num1\x18\x01 \x01(\x05\x12\x0c\n\x04num2\x18\x02 \x01(\x05\"\x1d\n\x0b\x41\x64\x64Response\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32Y\n\x11\x41\x63tivityPredictor\x12\x44\n\x03\x41\x64\x64\x12\x1d.activityPredictor.AddRequest\x1a\x1e.activityPredictor.AddResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'activityPredictor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ADDREQUEST']._serialized_start=46
  _globals['_ADDREQUEST']._serialized_end=86
  _globals['_ADDRESPONSE']._serialized_start=88
  _globals['_ADDRESPONSE']._serialized_end=117
  _globals['_ACTIVITYPREDICTOR']._serialized_start=119
  _globals['_ACTIVITYPREDICTOR']._serialized_end=208
# @@protoc_insertion_point(module_scope)
