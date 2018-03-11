import socket 
import struct
import textwrap

# Unpack ethernet frame
def ethernet_frame(data):
	dest_mec, src_mac, proto = struct.unpack('',)