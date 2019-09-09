import threading,os
def task1():
    print("current thread:",threading.current_thread().name)
    for i in range(25):
        print("task1")

def task2():
    print("current thread:",threading.current_thread().name)
    for i in range(25):
        print("task2")

print(threading.current_thread().name,os.getpid())
t1=threading.Thread(target=task1)
t1.start()
t2=threading.Thread (target=task2)
t2.start()
