from ctypes import *
from misc import Pos
from typing import Sequence, List


class LibTest:

    def __init__(self, lib_path) -> None:

        # 导入库 Windows中dll后缀名不需要加，但是Linux需要加
        # linux 系统下无法调用当前目录的.so文件，需要设置环境变量,不然就加载绝对路径
        try:
            self.lib = CDLL(lib_path)
        except:
            self.lib = CDLL(lib_path, winmode=0) # python 版本大于3.8

    def test_ctypes(self):
        return self.lib.test_ctypes()

    def test_ctypes_number(self, x: int , y: float, isNum: bool):
        return self.lib.test_ctypes_number(1, c_float(2.54), True)


    def test_string_a(self, text: str):
        text_byte = bytes(text, encoding="utf-8")
        return self.lib.test_string_a(text_byte, len(text_byte))

    def test_list(self, arr: Sequence[int]):
        ArrayType = c_int* len(arr)  # 根据数组长度创建的数组类型
        carr = ArrayType(*arr) # 把list每一个元素当作位置参数
        self.lib.test_list.argtypes = (ArrayType, )
        return self.lib.test_list(carr, len(arr))
    
    def test_string_w(self, text: str):
        return self.lib.test_string_w(text, len(text))

    def test_return_int(self):
        return self.lib.test_return_int()
    
    def test_return_char(self):
        self.lib.test_return_char.restype = c_char_p # 必须定义返回值类型，不然返回的就是一个地址
        return self.lib.test_return_char()   
    
    def test_return_wchar(self):
        self.lib.test_return_wchar.restype = c_wchar_p # 必须定义返回值类型，不然返回的就是一个地址
        return self.lib.test_return_wchar()

    def test_pointer(self, f1: float) :   
        self.lib.test_pointer.argtypes = (POINTER(c_float), ) # 传入参数类型
        self.lib.test_pointer.restype = (POINTER(c_int)) # 返回参数类型
        f1 = c_float(88.8)
        re = self.lib.test_pointer(f1)
        return re, f1

    def test_struct(self, pos1: Structure, pos2: Structure):
        self.lib.test_struct.argtypes = (Pos, POINTER(Pos))
        self.lib.test_struct(pos1, byref(pos2))

    def test_struct_list(self, array: List[Pos]):
        size = len(array)
        ArrayType = (Pos*size) 
        c_array = ArrayType(*array) # 把list每一个元素当作位置参数
        self.lib.test_struct_list.argtypes = (ArrayType, )
        self.lib.test_struct_list(c_array, size)
 