#include <iostream>


# ifdef _WIN32 
#define XLIB __declspec(dllexport)
#else
#define XLIB
#endif

#define EXTERN_C extern "C" XLIB 

// extern "C" C++中编译C格式的函数
//__declspec(dllexport) 函数导出到库中


/******************************
*           测试函数           *
*******************************/
EXTERN_C void test_ctypes()
{
	printf("in c test_cyptes\n");
	std::cout<<"in c test_cyptes"<<std::endl;
}


/******************************
*           测试传参           *
*******************************/
EXTERN_C void test_ctypes_number(int x, float y, bool isNum)
{
	printf("in c test_cyptes %d %f %d\n", x, y, isNum);
	if (isNum)
		printf("true");
	else
		printf("flase");
}

 EXTERN_C void test_string_a(char * text)
 {
    printf("test_string_a %s\n", text);
 }

EXTERN_C void test_string_w(wchar_t * text)
 {
    printf("test_string_w %ls\n", text);
 }

EXTERN_C void test_list(int * arr, int size)
 {
    for(int i = 0; i < size; i ++)
        std::cout<<arr[i];
    std::cout<<std::endl;
 }

/******************************
*          试返回值            *
*******************************/
EXTERN_C int test_return_int(wchar_t * text)
 {
    return 101;
 }

EXTERN_C char* test_return_char()
 {
    return "hello wrold\n";
 }


EXTERN_C wchar_t* test_return_wchar()
 {
    return L"hello wrold\n";
 }

/******************************
*      测试传递和返回指针       *
*******************************/

EXTERN_C int* test_pointer(float * f1)
{
    static int re = 1001;
    *f1 = 99.9;
    return  &re;
}


/******************************
*          测试结构体          *
*******************************/
struct Pos
{
   int x;
   int y;
};

EXTERN_C void test_struct(Pos pos1, Pos *pos2){
   std::cout <<"in C++ test sturct" << "\tpos1 x=" <<pos1.x <<"\tpos1 y=" << pos1.y<< std::endl;
   std::cout <<"in C++ test sturct" << "\tpos2 x=" <<pos2->x <<"\tpos2 y=" << pos2->y<< std::endl;
}

EXTERN_C void test_struct_list(Pos* pos, int size){
   for(int i = 0; i < size; i ++)
      std::cout <<"in C++ test sturct" << "\tpos1 x=" <<pos[i].x <<"\tpos1 y=" << pos[i].y<< std::endl;
}

/******************************
*         测试回调函数         *
*******************************/


typedef void (*Callback)(int a);

EXTERN_C void test_callback_func(Callback call, int *arr, int size)
{
   for (int i = 0; i < size; i++)
      call(arr[i]);
}
