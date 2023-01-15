from ctypes import Structure, c_int 


class Pos(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]

