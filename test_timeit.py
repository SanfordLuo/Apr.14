#coding=utf-8
print("===== from timeit import Timer =====")
# 直接导入timeit模块中的Timer方法
# 后起用的时候不用 timeit.Timer()，如25行
from timeit import Timer

def test1():
    li = []
    for i in range(10000):
        li.append(i)
def test2():
    li = []
    for i in range(10000):
        li += [i]
def test3():
    li = [i for i in range(10000)]
def test4():
    li = list(range(10000))
def test5():
    li = []
    for i in range(10000):
        li.insert(0, i)    # 指定位置添加，在下标索引0处添加i

if __name__ == '__main__':
    my_timer1 = Timer("test1()", "from __main__ import test1")
    print("test1的时间：%s" % my_timer1.timeit(1000))

    my_timer2 = Timer("test2()", "from __main__ import test2")
    print("test2的时间：%s" % my_timer2.timeit(1000))

    my_timer3 = Timer("test3()", "from __main__ import test3")
    print("test3的时间：%s" % my_timer3.timeit(1000))

    my_timer4 = Timer("test4()", "from __main__ import test4")
    print("test4的时间：%s" % my_timer4.timeit(1000))

    my_timer5 = Timer("test5()", "from __main__ import test5")
    print("test5的时间：%s" % my_timer5.timeit(1000))

print("===== import timeit =====")
# 导入模块 后期引用方法需要用 timeit.Timer()， 如46行
import timeit
def test():
    li = [i for i in range(1000)]

my_timer = timeit.Timer("test()","from __main__ import test")
ret = my_timer.timeit(1000)
print(ret)
