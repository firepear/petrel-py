"""petrel_pyclient is a Python port of the client of the Petrel
networking library
"""

#import socket
#import struct

# https://www.digitalocean.com/community/tutorials/python-string-encode-decode
#
# bytearray(b'') is what we probably want for constructing/receiving
# things over the network. encode gets you a bytes object, which is
# immutable; bytearray can do append() as well as be sliced back into
# bytes. between that and struct.(un)pack, getting data to/from the
# network should be covered
