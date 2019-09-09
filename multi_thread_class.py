import threading,time
class my_thread(threading.Thread):
    def run(self):
        for i in range(25):
            print("my thread")

class other_thread(threading.Thread):
    def run(self):
        for i in range(25):
            print("other thread")

begin=time.time()
m1=my_thread()
o1=other_thread()
m1.start()
o1.start()
m1.join()
o1.join()
close=time.time()
print(close-begin)## if not join inbetween else join atlast
