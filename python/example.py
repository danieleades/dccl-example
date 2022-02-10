__version__ = "0.1.0"

import os

import dccl

from sb_dccl import navreport_pb2

# dccl.addProtoIncludePath(os.path.abspath("."))
# dccl.addProtoIncludePath(os.path.abspath("../dccl/include"))

dccl.loadProtoFile(os.path.abspath("../proto/navreport.proto"))

codec = dccl.Codec()
codec.load("NavigationReport")

# SENDER
r_out = navreport_pb2.NavigationReport(
    x=450.01,
    y=550,
    z=-100,
    veh_class=navreport_pb2.NavigationReport.AUV,
    battery_ok=True,
)
encoded_bytes = codec.encode(r_out)

# send encoded_bytes across your link

print(f"encoded_bytes: {encoded_bytes}")
print(f"number of bytes: {len(encoded_bytes)}")

# RECEIVER
decoded_msg = codec.decode(encoded_bytes)
print(decoded_msg)
