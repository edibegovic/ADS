from algs4.stdlib.stdrandom import uniformInt,shuffle
from algs4.stdlib.stdstats import mean,stddev
#from algs4.stdlib.stdio import eprint
from random import randint 

import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class RandomQueue:
    q = []
    q_size = 0

    def __init__(self):
        None

    def isEmpty(self):
        return (not bool(self.q_size))
        
    def size(self):
        return self.q_size
        
    def __len__(self):
        return self.size()
        
    def enqueue(self,item):
        if self.q_size != len(self.q):
            self.q[self.q_size] = item
        else:
            self.q.append(item)
        self.q_size += 1
        
    def sample(self):
        if self.isEmpty():
            return "nope" 
        return(self.q[randint(0, self.q_size-1)]) 

    def dequeue(self):
        if self.isEmpty():
            return "nope" 
        random_idx = randint(0, self.q_size-1)
        return_value = self.q[random_idx]
        self.q[random_idx] = self.q[self.q_size-1]
        self.q_size -= 1
        return return_value

    def __iter__(self):
        temp_q = self.q
        temp_size = self.size()
        mine = []

        while not self.isEmpty():
            mine.append(self.dequeue())

        self.q = temp_q
        self.q_size = temp_size

        for x in mine:
            yield x


# This  "main method" tests your implementation. Do not change it.
if __name__ == '__main__':
    Q = RandomQueue()
    # build a randomQueue with 1,2,..,6
    for i in range(1,7):
        Q.enqueue(i)
        
    # print 30 die rolls
    eprint( ' '.join([str(Q.sample()) for i in range(30) ] ) )

    # Let's be more serious: do they really behave like die rolls?
    rolls = [ Q.sample() for i in range(1000) ]
    eprint("Mean (should be around 3.5): {:5.4f}".format(mean(rolls)))
    eprint("Standard deviation (should be around 1.7): {:5.4f}".format(stddev(rolls)))

    # removing 3 random values
    eprint( "Removing {}".format(' '.join( [str(Q.dequeue()) for i in range(3) ] ) ) )
    
    #Add 7,8,9
    for i in range(7,10):
        Q.enqueue(i); 
    # Empty the queue in random order
    while not Q.isEmpty():
        eprint(Q.dequeue(),end=' ');
    eprint()

    # Let s look at the iterator. First, we make a queue of colours:
    C= RandomQueue()
    C.enqueue("red"); C.enqueue("blue"); C.enqueue("green"); C.enqueue("yellow"); 

    I = iter(C)
    J = iter(C)

    eprint("Two colours from first shuffle: {} {}".format(next(I),next(I)))
    
    eprint("Entire second shuffle: {}".format(' '.join([i for i in J])));

    eprint("Remaining two colours from first shuffle: {} {}".format(next(I),next(I)))

    # for i in range(3):
    #     eprint(list( Q))
    # for i in range(6):
    #     eprint(Q.dequeue())
    

