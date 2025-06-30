from typing import TypedDict
import random
import time
import logging
import threading

class Notification:

    def __init__(self, text: str, created_at=time.time()):
    
        self.data = [text, created_at]


    def get(self):

        return(self.data)


class NotificationQueue:

    def __init__(self):

        self.queue = list()  # It does not use linked-list structure, 'cause lists are more simply.
        self.head = 0
        self.empty_counter = 5
        self.lock = threading.Lock() # It uses just only one mutex for all operations with the queue.


    def new(self, n: Notification) -> bool:

        self.lock.acquire()  # The class uses len(self.queue) in many cases and changes the length of the queue.
        self.queue.append(n)
        self.lock.release()

        return(True)
    

    def pop(self) -> Notification:  # O(1)

        if len(self.queue) > 0 and self.head < len(self.queue):

            self.lock.acquire()
            ret = self.queue[self.head]
            self.head += 1
            self.lock.release()

            # The time to clear the firsts elements of the queue to avoid memory leaks.
            # [a, b, c, d, e] -> [c, d, e] 
            #        ^            ^
            #        head = 2     head = 0

            if self.head > self.empty_counter:

                # A lock to avoid 'len()' and 'head' changes in an another thread. 

                self.lock.acquire()
                self.queue = self.queue[self.head:len(self.queue)]
                self.head = 0
                self.lock.release()

                logging.warning('Queue is cleared, old len: {}, new len: {}'.format(len(self.queue) + self.empty_counter, len(self.queue)))

            return(ret)
        
        return(None)


    def getRandom(self) -> Notification:

        if len(self.queue) > 0 and self.head < len(self.queue): 
            
            # A lock to avoid "index out of range situation"

            self.lock.acquire()
            ret = self.queue[random.randint(self.head, len(self.queue) - 1)]
            self.lock.release()

            return(ret)
            
        
        return(None)


"""
from nq import Notification
from nq import NotificationQueue

notification1 = Notification('first', 111)
notification2 = Notification('second')
notification3 = Notification('third')


q = NotificationQueue()

q.new(notification1)
q.new(notification2)
q.new(notification3)

ret1 = q.pop()
ret2 = q.getRandom()
ret3 = q.pop()

print(ret1.get())
print(ret2.get())
print(ret3.get())

print()

for i in range(15):

    n = Notification2 = Notification('msg {}'.format(i))
    q.new(n)

for i in range(14):

    print(q.pop().get())
"""
