# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rmessage.proto\"D\n\x04Mess\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x13\n\x0b\x66ullmessage\x18\x04 \x01(\t\"\x1c\n\x05Inbox\x12\x13\n\x04msgg\x18\x01 \x03(\x0b\x32\x05.Messb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MESS = _descriptor.Descriptor(
  name='Mess',
  full_name='Mess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Mess.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Mess.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='Mess.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fullmessage', full_name='Mess.fullmessage', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=85,
)


_INBOX = _descriptor.Descriptor(
  name='Inbox',
  full_name='Inbox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgg', full_name='Inbox.msgg', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=115,
)

_INBOX.fields_by_name['msgg'].message_type = _MESS
DESCRIPTOR.message_types_by_name['Mess'] = _MESS
DESCRIPTOR.message_types_by_name['Inbox'] = _INBOX

Mess = _reflection.GeneratedProtocolMessageType('Mess', (_message.Message,), dict(
  DESCRIPTOR = _MESS,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:Mess)
  ))
_sym_db.RegisterMessage(Mess)

Inbox = _reflection.GeneratedProtocolMessageType('Inbox', (_message.Message,), dict(
  DESCRIPTOR = _INBOX,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:Inbox)
  ))
_sym_db.RegisterMessage(Inbox)


# @@protoc_insertion_point(module_scope)
