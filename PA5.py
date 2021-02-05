#Written by Charlie Irmiger
#Using a heap data structure for finding median in O(log(n)) time

import heapq
class Median:
    def __init__(self):
        self.small = []
        self.big = []
    def peek_big(self):
        if not self.big:
            return 0
        return self.big[0]
    def peek_small(self):
        if not self.small:
            return 0
        return -self.small[0]
    def pop_big(self):
        return heapq.heappop(self.big)
    def pop_small(self):
        return - heapq.heappop(self.small)
    def add_small(self, element):
        heapq.heappush(self.small, -element)
    def add_big(self, element):
        heapq.heappush(self.big, element)


    def get_length(self):
        if self.small:
            return len(self.small)
        if self.big:
            return len(self.big)

    def get_median(self):
        if len(self.small) == len(self.big):
            return (self.peek_big() + self.peek_small()) / 2
        else:
            return self.peek_big()
        

    def add(self, element):
        if len(self.big) == len(self.small):                        #balanced
            if not element < self.peek_small():                     #element valid larger than big[0]
                self.add_big(element)
            else:                                                   #else move max of small to big, add element to small
                self.add_big(self.pop_small())
                self.add_small(element)
        elif len(self.big) > len(self.small):
            if element > self.peek_big():
                self.add_small(self.pop_big())
                self.add_big(element)
            else:
                self.add_small(element)

    def is_in(self, element):
        #dont know why this would be needed
        pass



def test():
    m = Median()
    for i in [1,3,1,4,5,6,1,2,4,3,8,9,1,2,2,1,6,
              7, 1, 1, 1, 1, 1, 2,1,1,1,1,1,1,1]:
        m.add(i)
        print('inserted', i)
        print(([-x for x in sorted(m.small)][::-1]), sorted(m.big))
        print('median is now', m.get_median())

test()
