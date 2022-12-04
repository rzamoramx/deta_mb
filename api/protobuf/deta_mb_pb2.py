# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/protobuf/deta_mb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/protobuf/deta_mb.proto',
  package='detamb',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x61pi/protobuf/deta_mb.proto\x12\x06\x64\x65tamb\"8\n\x03Msg\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\",\n\x0bRespPulling\x12\x1d\n\x08messages\x18\x01 \x03(\x0b\x32\x0b.detamb.Msg\"B\n\x04Resp\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x0b\n\x03\x61\x63k\x18\x03 \x01(\x05\x12\x0e\n\x06\x64\x65tail\x18\x04 \x01(\t\"X\n\x03Req\x12\r\n\x05topic\x18\x01 \x01(\t\x12\r\n\x05\x61\x63ked\x18\x02 \x01(\x05\x12\x10\n\x08timefrom\x18\x03 \x01(\x03\x12\x0e\n\x06timeto\x18\x04 \x01(\x03\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\x62\x06proto3'
)




_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='detamb.Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='detamb.Msg.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='detamb.Msg.payload', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='detamb.Msg.timestamp', index=2,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=94,
)


_RESPPULLING = _descriptor.Descriptor(
  name='RespPulling',
  full_name='detamb.RespPulling',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='detamb.RespPulling.messages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=140,
)


_RESP = _descriptor.Descriptor(
  name='Resp',
  full_name='detamb.Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='detamb.Resp.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='detamb.Resp.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ack', full_name='detamb.Resp.ack', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detail', full_name='detamb.Resp.detail', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=208,
)


_REQ = _descriptor.Descriptor(
  name='Req',
  full_name='detamb.Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='detamb.Req.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acked', full_name='detamb.Req.acked', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timefrom', full_name='detamb.Req.timefrom', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeto', full_name='detamb.Req.timeto', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='detamb.Req.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=298,
)

_RESPPULLING.fields_by_name['messages'].message_type = _MSG
DESCRIPTOR.message_types_by_name['Msg'] = _MSG
DESCRIPTOR.message_types_by_name['RespPulling'] = _RESPPULLING
DESCRIPTOR.message_types_by_name['Resp'] = _RESP
DESCRIPTOR.message_types_by_name['Req'] = _REQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), {
  'DESCRIPTOR' : _MSG,
  '__module__' : 'api.protobuf.deta_mb_pb2'
  # @@protoc_insertion_point(class_scope:detamb.Msg)
  })
_sym_db.RegisterMessage(Msg)

RespPulling = _reflection.GeneratedProtocolMessageType('RespPulling', (_message.Message,), {
  'DESCRIPTOR' : _RESPPULLING,
  '__module__' : 'api.protobuf.deta_mb_pb2'
  # @@protoc_insertion_point(class_scope:detamb.RespPulling)
  })
_sym_db.RegisterMessage(RespPulling)

Resp = _reflection.GeneratedProtocolMessageType('Resp', (_message.Message,), {
  'DESCRIPTOR' : _RESP,
  '__module__' : 'api.protobuf.deta_mb_pb2'
  # @@protoc_insertion_point(class_scope:detamb.Resp)
  })
_sym_db.RegisterMessage(Resp)

Req = _reflection.GeneratedProtocolMessageType('Req', (_message.Message,), {
  'DESCRIPTOR' : _REQ,
  '__module__' : 'api.protobuf.deta_mb_pb2'
  # @@protoc_insertion_point(class_scope:detamb.Req)
  })
_sym_db.RegisterMessage(Req)


# @@protoc_insertion_point(module_scope)
