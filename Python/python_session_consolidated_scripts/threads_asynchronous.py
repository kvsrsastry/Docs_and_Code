# Threading
import threading
import time, datetime

class mythread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name=name
        self.delay=delay
        print('{} created successfully'.format(name))

    def run(self):
        print('{} Started'.format(self.name))
        process(self.name, self.delay)
        print('{} Done'.format(self.name))

def process(name,delay):
    counter = 5
    while counter != 0:
        print('{} : {}'.format(name, datetime.datetime.now()))
        time.sleep(delay)
        counter = counter - 1

t1 = mythread('Thread-1', 1)
t2 = mythread('Thread-2', 2)
t1.start()
t2.start()
t1.join()
t2.join()
print('End of the Main Thread')
