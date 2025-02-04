# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/FeatureTable.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from proto.v012.feast.core import DataSource_pb2 as feast_dot_core_dot_DataSource__pb2
from proto.v012.feast.core import Feature_pb2 as feast_dot_core_dot_Feature__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/core/FeatureTable.proto',
  package='feast.core',
  syntax='proto3',
  serialized_options=b'\n\020feast.proto.coreB\021FeatureTableProtoZ3github.com/feast-dev/feast/sdk/go/protos/feast/core',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x66\x65\x61st/core/FeatureTable.proto\x12\nfeast.core\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1b\x66\x65\x61st/core/DataSource.proto\x1a\x18\x66\x65\x61st/core/Feature.proto\"f\n\x0c\x46\x65\x61tureTable\x12*\n\x04spec\x18\x01 \x01(\x0b\x32\x1c.feast.core.FeatureTableSpec\x12*\n\x04meta\x18\x02 \x01(\x0b\x32\x1c.feast.core.FeatureTableMeta\"\xe2\x02\n\x10\x46\x65\x61tureTableSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\t \x01(\t\x12\x10\n\x08\x65ntities\x18\x03 \x03(\t\x12+\n\x08\x66\x65\x61tures\x18\x04 \x03(\x0b\x32\x19.feast.core.FeatureSpecV2\x12\x38\n\x06labels\x18\x05 \x03(\x0b\x32(.feast.core.FeatureTableSpec.LabelsEntry\x12*\n\x07max_age\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12,\n\x0c\x62\x61tch_source\x18\x07 \x01(\x0b\x32\x16.feast.core.DataSource\x12-\n\rstream_source\x18\x08 \x01(\x0b\x32\x16.feast.core.DataSource\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa5\x01\n\x10\x46\x65\x61tureTableMeta\x12\x35\n\x11\x63reated_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16last_updated_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08revision\x18\x03 \x01(\x03\x12\x0c\n\x04hash\x18\x04 \x01(\tBZ\n\x10\x66\x65\x61st.proto.coreB\x11\x46\x65\x61tureTableProtoZ3github.com/feast-dev/feast/sdk/go/protos/feast/coreb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,feast_dot_core_dot_DataSource__pb2.DESCRIPTOR,feast_dot_core_dot_Feature__pb2.DESCRIPTOR,])




_FEATURETABLE = _descriptor.Descriptor(
  name='FeatureTable',
  full_name='feast.core.FeatureTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='spec', full_name='feast.core.FeatureTable.spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='feast.core.FeatureTable.meta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=165,
  serialized_end=267,
)


_FEATURETABLESPEC_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='feast.core.FeatureTableSpec.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.core.FeatureTableSpec.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.core.FeatureTableSpec.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=579,
  serialized_end=624,
)

_FEATURETABLESPEC = _descriptor.Descriptor(
  name='FeatureTableSpec',
  full_name='feast.core.FeatureTableSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.core.FeatureTableSpec.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project', full_name='feast.core.FeatureTableSpec.project', index=1,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entities', full_name='feast.core.FeatureTableSpec.entities', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='features', full_name='feast.core.FeatureTableSpec.features', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='feast.core.FeatureTableSpec.labels', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_age', full_name='feast.core.FeatureTableSpec.max_age', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_source', full_name='feast.core.FeatureTableSpec.batch_source', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stream_source', full_name='feast.core.FeatureTableSpec.stream_source', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FEATURETABLESPEC_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=624,
)


_FEATURETABLEMETA = _descriptor.Descriptor(
  name='FeatureTableMeta',
  full_name='feast.core.FeatureTableMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='created_timestamp', full_name='feast.core.FeatureTableMeta.created_timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_updated_timestamp', full_name='feast.core.FeatureTableMeta.last_updated_timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision', full_name='feast.core.FeatureTableMeta.revision', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='feast.core.FeatureTableMeta.hash', index=3,
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
  serialized_start=627,
  serialized_end=792,
)

_FEATURETABLE.fields_by_name['spec'].message_type = _FEATURETABLESPEC
_FEATURETABLE.fields_by_name['meta'].message_type = _FEATURETABLEMETA
_FEATURETABLESPEC_LABELSENTRY.containing_type = _FEATURETABLESPEC
_FEATURETABLESPEC.fields_by_name['features'].message_type = feast_dot_core_dot_Feature__pb2._FEATURESPECV2
_FEATURETABLESPEC.fields_by_name['labels'].message_type = _FEATURETABLESPEC_LABELSENTRY
_FEATURETABLESPEC.fields_by_name['max_age'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_FEATURETABLESPEC.fields_by_name['batch_source'].message_type = feast_dot_core_dot_DataSource__pb2._DATASOURCE
_FEATURETABLESPEC.fields_by_name['stream_source'].message_type = feast_dot_core_dot_DataSource__pb2._DATASOURCE
_FEATURETABLEMETA.fields_by_name['created_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FEATURETABLEMETA.fields_by_name['last_updated_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['FeatureTable'] = _FEATURETABLE
DESCRIPTOR.message_types_by_name['FeatureTableSpec'] = _FEATURETABLESPEC
DESCRIPTOR.message_types_by_name['FeatureTableMeta'] = _FEATURETABLEMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeatureTable = _reflection.GeneratedProtocolMessageType('FeatureTable', (_message.Message,), {
  'DESCRIPTOR' : _FEATURETABLE,
  '__module__' : 'feast.core.FeatureTable_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.FeatureTable)
  })
_sym_db.RegisterMessage(FeatureTable)

FeatureTableSpec = _reflection.GeneratedProtocolMessageType('FeatureTableSpec', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEATURETABLESPEC_LABELSENTRY,
    '__module__' : 'feast.core.FeatureTable_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.FeatureTableSpec.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _FEATURETABLESPEC,
  '__module__' : 'feast.core.FeatureTable_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.FeatureTableSpec)
  })
_sym_db.RegisterMessage(FeatureTableSpec)
_sym_db.RegisterMessage(FeatureTableSpec.LabelsEntry)

FeatureTableMeta = _reflection.GeneratedProtocolMessageType('FeatureTableMeta', (_message.Message,), {
  'DESCRIPTOR' : _FEATURETABLEMETA,
  '__module__' : 'feast.core.FeatureTable_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.FeatureTableMeta)
  })
_sym_db.RegisterMessage(FeatureTableMeta)


DESCRIPTOR._options = None
_FEATURETABLESPEC_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
