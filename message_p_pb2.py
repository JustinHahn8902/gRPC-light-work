# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message_p.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fmessage_p.proto\".\n\rClientMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\" \n\rServerMessage\x12\x0f\n\x07message\x18\x01 \x01(\t2\xd4\x01\n\tMessaging\x12/\n\rSingleMessage\x12\x0e.ClientMessage\x1a\x0e.ServerMessage\x12\x30\n\x0cServerStream\x12\x0e.ClientMessage\x1a\x0e.ServerMessage0\x01\x12\x30\n\x0c\x43lientStream\x12\x0e.ClientMessage\x1a\x0e.ServerMessage(\x01\x12\x32\n\x0cTwoWayStream\x12\x0e.ClientMessage\x1a\x0e.ServerMessage(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_p_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CLIENTMESSAGE']._serialized_start=19
  _globals['_CLIENTMESSAGE']._serialized_end=65
  _globals['_SERVERMESSAGE']._serialized_start=67
  _globals['_SERVERMESSAGE']._serialized_end=99
  _globals['_MESSAGING']._serialized_start=102
  _globals['_MESSAGING']._serialized_end=314
# @@protoc_insertion_point(module_scope)