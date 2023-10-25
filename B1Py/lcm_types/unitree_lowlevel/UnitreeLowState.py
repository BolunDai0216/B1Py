"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct


class UnitreeLowState:
    __slots__ = [
        "stamp",
        "q",
        "dq",
        "tau_est",
        "contact_state",
        "accel",
        "gyro",
        "temperature",
        "quaternion",
        "rpy",
        "gravity",
        "gt_pos",
        "gt_quat",
        "gt_lin_vel",
        "gt_ang_vel",
    ]

    __typenames__ = [
        "double",
        "float",
        "float",
        "float",
        "float",
        "float",
        "float",
        "float",
        "float",
        "float",
        "float",
        "float",
        "float",
        "float",
        "float",
    ]

    __dimensions__ = [
        None,
        [12],
        [12],
        [12],
        [4],
        [3],
        [3],
        None,
        [4],
        [3],
        [3],
        [3],
        [4],
        [3],
        [3],
    ]

    def __init__(self):
        self.stamp = 0.0
        self.q = [0.0 for dim0 in range(12)]
        self.dq = [0.0 for dim0 in range(12)]
        self.tau_est = [0.0 for dim0 in range(12)]
        self.contact_state = [0.0 for dim0 in range(4)]
        self.accel = [0.0 for dim0 in range(3)]
        self.gyro = [0.0 for dim0 in range(3)]
        self.temperature = 0.0
        self.quaternion = [0.0 for dim0 in range(4)]
        self.rpy = [0.0 for dim0 in range(3)]
        self.gravity = [0.0 for dim0 in range(3)]
        self.gt_pos = [0.0 for dim0 in range(3)]
        self.gt_quat = [0.0 for dim0 in range(4)]
        self.gt_lin_vel = [0.0 for dim0 in range(3)]
        self.gt_ang_vel = [0.0 for dim0 in range(3)]

    def encode(self):
        buf = BytesIO()
        buf.write(UnitreeLowState._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">d", self.stamp))
        buf.write(struct.pack(">12f", *self.q[:12]))
        buf.write(struct.pack(">12f", *self.dq[:12]))
        buf.write(struct.pack(">12f", *self.tau_est[:12]))
        buf.write(struct.pack(">4f", *self.contact_state[:4]))
        buf.write(struct.pack(">3f", *self.accel[:3]))
        buf.write(struct.pack(">3f", *self.gyro[:3]))
        buf.write(struct.pack(">f", self.temperature))
        buf.write(struct.pack(">4f", *self.quaternion[:4]))
        buf.write(struct.pack(">3f", *self.rpy[:3]))
        buf.write(struct.pack(">3f", *self.gravity[:3]))
        buf.write(struct.pack(">3f", *self.gt_pos[:3]))
        buf.write(struct.pack(">4f", *self.gt_quat[:4]))
        buf.write(struct.pack(">3f", *self.gt_lin_vel[:3]))
        buf.write(struct.pack(">3f", *self.gt_ang_vel[:3]))

    def decode(data):
        if hasattr(data, "read"):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != UnitreeLowState._get_packed_fingerprint():
            raise ValueError("Decode error")
        return UnitreeLowState._decode_one(buf)

    decode = staticmethod(decode)

    def _decode_one(buf):
        self = UnitreeLowState()
        self.stamp = struct.unpack(">d", buf.read(8))[0]
        self.q = struct.unpack(">12f", buf.read(48))
        self.dq = struct.unpack(">12f", buf.read(48))
        self.tau_est = struct.unpack(">12f", buf.read(48))
        self.contact_state = struct.unpack(">4f", buf.read(16))
        self.accel = struct.unpack(">3f", buf.read(12))
        self.gyro = struct.unpack(">3f", buf.read(12))
        self.temperature = struct.unpack(">f", buf.read(4))[0]
        self.quaternion = struct.unpack(">4f", buf.read(16))
        self.rpy = struct.unpack(">3f", buf.read(12))
        self.gravity = struct.unpack(">3f", buf.read(12))
        self.gt_pos = struct.unpack(">3f", buf.read(12))
        self.gt_quat = struct.unpack(">4f", buf.read(16))
        self.gt_lin_vel = struct.unpack(">3f", buf.read(12))
        self.gt_ang_vel = struct.unpack(">3f", buf.read(12))
        return self

    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if UnitreeLowState in parents:
            return 0
        tmphash = (0x63FBA9EF911D1605) & 0xFFFFFFFFFFFFFFFF
        tmphash = (
            ((tmphash << 1) & 0xFFFFFFFFFFFFFFFF) + (tmphash >> 63)
        ) & 0xFFFFFFFFFFFFFFFF
        return tmphash

    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if UnitreeLowState._packed_fingerprint is None:
            UnitreeLowState._packed_fingerprint = struct.pack(
                ">Q", UnitreeLowState._get_hash_recursive([])
            )
        return UnitreeLowState._packed_fingerprint

    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", UnitreeLowState._get_packed_fingerprint())[0]
