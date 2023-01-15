import os
import sys
from test_ctypes import LibTest, Pos
from misc import Pos

lib_path = os.path.join(os.getcwd(), "libs", "test_ctypes")
if sys.platform == "linux":
    lib_path += ".so"

lib = LibTest(lib_path)
print("-"*40 + "测试函数" + "-"*40)
lib.test_ctypes()

print("-"*40 + "测试传参" + "-"*40)
lib.test_ctypes_number(1, 2.54, True)   # 传递int float bool
lib.test_string_a("hello")              # 传递窄字符
lib.test_string_w("world")              # 传递宽字符
lib.test_list([1, 2, 3, 4, 5])          # 传递数组
lib.test_struct(Pos(11, 22), Pos(33,44))            # 传递结构体
lib.test_struct_list([Pos(11, 22), Pos(33,44)])            # 传递结构体数组


print("-"*40 + "测试返回值" + "-"*40)
print(lib.test_return_int())
print(lib.test_return_char(), "type:", type(lib.test_return_char()))
print(lib.test_return_wchar(), "type:", type(lib.test_return_wchar()))

print("-"*40 + "测试传递和返回指针" + "-"*40)
f1 = 8.8
print("before test_pointer:", f1)
re, f1 = lib.test_pointer(f1)
print("after test_pointer:", f1)
print("return ", re, "type:", type(re), "pointer value:", re.contents.value)
