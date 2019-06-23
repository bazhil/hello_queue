from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue

words = ['first', 'second', 'third']

numbers = list(range(10))

squared_numbers = [i**2 for i in range(20) if i%2!=0]

def fifo_queue(words):
    """
    Function demonstrated FIFO queue
    :param words: list of words
    :return:
    """
    print('FIFO queue. Print items of list in same order with it was appended.')
    q = Queue()

    for word in words:
        q.put(word)
    print('Queue size is: ', q.qsize())

    while not q.empty():
        print(q.get())
    print('Queue is full?', q.full(), '\n')


def lifo_queue(numbers):
    """
    Function, which demonstate LIFO queue.
    :param numbers: list of numbers
    :return:
    """
    print('LIFO queue. Print items of list in opposite order with it was appended.')
    lq = LifoQueue()

    for number in numbers:
        lq.put(number)
    print('Queue size is: ', lq.qsize())

    while not lq.empty():
        print(lq.get())
    print('Queue is full?', lq.full(), '\n')


# Priority queue
def priority_queue():
    """
    Function which demonstrate Priority queue
    :return:
    """
    print('Priority queue. Print items from 10 to 1 in corresponding order with it priority.')
    pq = PriorityQueue()

    pq.put(10, 'ten')
    pq.put(9, 'nine')
    pq.put(8, 'eight')
    pq.put(7, 'seven')
    pq.put(6, 'six')
    pq.put(5, 'five')
    pq.put(4, 'four')
    pq.put(3, 'three')
    pq.put(2, 'two')
    pq.put(1, 'one')
    print('Queue size is: ', pq.qsize())

    while not pq.empty():
        print(pq.get())
    print('Queue is full?', pq.full(), '\n')

if __name__ == '__main__':
    fifo_queue(words)
    lifo_queue(numbers)
    priority_queue()