python -m grpc_tools.protoc -I shurl/grpc/definitions/ --python_out=shurl/grpc/definitions/builds/ \
--grpc_python_out=shurl/grpc/definitions/builds/ shurl/grpc/definitions/service.proto
