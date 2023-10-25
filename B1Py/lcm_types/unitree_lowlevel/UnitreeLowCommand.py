"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

from io import BytesIO
import struct

class UnitreeLowCommand(object):
    __slots__ = ["stamp", "tau_ff", "q_des", "dq_des", "kp", "kd"]

    __typenames__ = ["double", "float", "float", "float", "float", "float"]

    __dimensions__ = [None, [12], [12], [12], [12], [12]]

    def __init__(self):
        self.stamp = 0.0
        self.tau_ff = [ 0.0 for dim0 in range(12) ]
        self.q_des = [ 0.0 for dim0 in range(12) ]
        self.dq_des = [ 0.0 for dim0 in range(12) ]
        self.kp = [ 0.0 for dim0 in range(12) ]
        self.kd = [ 0.0 for dim0 in range(12) ]

    def encode(self):
        buf = BytesIO()
        buf.write(UnitreeLowCommand._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">d", self.stamp))
        buf.write(struct.pack('>12f', *self.tau_ff[:12]))
        buf.write(struct.pack('>12f', *self.q_des[:12]))
        buf.write(struct.pack('>12f', *self.dq_des[:12]))
        buf.write(struct.pack('>12f', *self.kp[:12]))
        buf.write(struct.pack('>12f', *self.kd[:12]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != UnitreeLowCommand._get_packed_fingerprint():
            raise ValueError("Decode error")
        return UnitreeLowCommand._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = UnitreeLowCommand()
        self.stamp = struct.unpack(">d", buf.read(8))[0]
        self.tau_ff = struct.unpack('>12f', buf.read(48))
        self.q_des = struct.unpack('>12f', buf.read(48))
        self.dq_des = struct.unpack('>12f', buf.read(48))
        self.kp = struct.unpack('>12f', buf.read(48))
        self.kd = struct.unpack('>12f', buf.read(48))
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if UnitreeLowCommand in parents: return 0
        tmphash = (0x3fa55736ccae518d) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if UnitreeLowCommand._packed_fingerprint is None:
            UnitreeLowCommand._packed_fingerprint = struct.pack(">Q", UnitreeLowCommand._get_hash_recursive([]))
        return UnitreeLowCommand._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", UnitreeLowCommand._get_packed_fingerprint())[0]
