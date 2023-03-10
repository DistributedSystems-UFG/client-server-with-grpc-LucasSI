# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EmployeeService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x45mployeeService.proto\x12\x10\x65mployee_service\"7\n\x0c\x45mployeeData\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\x1d\n\x0bStatusReply\x12\x0e\n\x06status\x18\x01 \x01(\t\"\x18\n\nEmployeeID\x12\n\n\x02id\x18\x01 \x01(\r\"0\n\x13\x45mployeeTitleUpdate\x12\n\n\x02id\x18\x01 \x01(\r\x12\r\n\x05title\x18\x02 \x01(\t\"\x0e\n\x0c\x45mptyMessage\"I\n\x10\x45mployeeDataList\x12\x35\n\remployee_data\x18\x01 \x03(\x0b\x32\x1e.employee_service.EmployeeData2\xf5\x04\n\x0f\x45mployeeService\x12Q\n\x0e\x43reateEmployee\x12\x1e.employee_service.EmployeeData\x1a\x1d.employee_service.StatusReply\"\x00\x12W\n\x15GetEmployeeDataFromID\x12\x1c.employee_service.EmployeeID\x1a\x1e.employee_service.EmployeeData\"\x00\x12]\n\x13UpdateEmployeeTitle\x12%.employee_service.EmployeeTitleUpdate\x1a\x1d.employee_service.StatusReply\"\x00\x12O\n\x0e\x44\x65leteEmployee\x12\x1c.employee_service.EmployeeID\x1a\x1d.employee_service.StatusReply\"\x00\x12X\n\x10ListAllEmployees\x12\x1e.employee_service.EmptyMessage\x1a\".employee_service.EmployeeDataList\"\x00\x12U\n\x12\x44\x65leteAllEmployees\x12\x1e.employee_service.EmptyMessage\x1a\x1d.employee_service.StatusReply\"\x00\x12U\n\rSortEmployees\x12\x1e.employee_service.EmptyMessage\x1a\".employee_service.EmployeeDataList\"\x00\x42\x37\n\x1bio.grpc.examples.iotserviceB\x0fIoTServiceProtoP\x01\xa2\x02\x04TEMPb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'EmployeeService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033io.grpc.examples.iotserviceB\017IoTServiceProtoP\001\242\002\004TEMP'
  _EMPLOYEEDATA._serialized_start=43
  _EMPLOYEEDATA._serialized_end=98
  _STATUSREPLY._serialized_start=100
  _STATUSREPLY._serialized_end=129
  _EMPLOYEEID._serialized_start=131
  _EMPLOYEEID._serialized_end=155
  _EMPLOYEETITLEUPDATE._serialized_start=157
  _EMPLOYEETITLEUPDATE._serialized_end=205
  _EMPTYMESSAGE._serialized_start=207
  _EMPTYMESSAGE._serialized_end=221
  _EMPLOYEEDATALIST._serialized_start=223
  _EMPLOYEEDATALIST._serialized_end=296
  _EMPLOYEESERVICE._serialized_start=299
  _EMPLOYEESERVICE._serialized_end=928
# @@protoc_insertion_point(module_scope)                                                                                                                                                                            38,1          Bot                                                                                                                                                                                            1,1           Top
