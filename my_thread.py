import threading, time
"""
方案1
使用一个子线程执行多个任务
"""
def work1():
    for i in range(5):
        print("work1")
        time.sleep(0.1)
def work2():
    for i in range(5):
        print("work2")
        time.sleep(0.1)
def func():
    work1()
    work2()

if __name__ == '__main__':
    func_thread = threading.Thread(target=func())
    func_thread.start()

print("="*20)
"""
方案2
自定义线程
"""
class MyThread(threading.Thread):
    # 重写init方法
    def __init__(self, name):
        # 如果自定义线程类，而且重写父类init方法，必须调用下父类的init方法
        super(MyThread, self).__init__()
        self.name = name
    def work3(self):
        for i in range(5):
            print("work3")
            time.sleep(0.1)
    def work4(self):
        for i in range(5):
            print("work4")
            time.sleep(0.1)
    def run(self):
        self.work3()
        self.work4()

if __name__ == '__main__':
    my_thread = MyThread("自定义线程")
    my_thread.start()
