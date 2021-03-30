import random
from datetime import *


class Node:
    def __init__(self, num=None):
        self.num = num
        self.next = None


class ALGORITHMS:
    def __init__(self):
        self.fp = open("hanno.txt", 'a+')
        # self.fp.writelines('haha\n')
        # self.fp.writelines('secondline\n')
        # self.fp.close()
        pass

    def binary_search(self, S, num, begin, end):
        if begin > end:
            return None
        mid = (begin + end) // 2
        if S[mid] == num:
            print(S[max(0,mid-2):min(mid+2, len(S))])
            print(mid, S[mid])
            return mid
        elif mid < num:
            self.binary_search(S, num, mid+1, end)
        else:
            self.binary_search(S, num, begin, mid-1)

    def max_ele(self, x, y):
        if y == 0:
            return x
        x, y = y, x % y
        return self.max_ele(x, y)

    def min_ele(self, x, y):
        return x * y // self.max_ele(x, y)

    def hanluota(self, num, left, mid, right):
        if num == 1:
            self.fp.writelines(f'{left}-->{right}\n')
            return
        self.hanluota(num-1, left, right, mid)
        self.fp.writelines(f'{left}-->{right}\n')
        self.hanluota(num-1, mid, left, right)

    def node_op(self):
        node_list = [Node(i) for i in range(5)]
        for i in range(len(node_list)-1):
            node_list[i].next = node_list[i+1]
        head = node_list[0]
        while head:
            print(head.num)
            head = head.next

    def running(self):
        day = timedelta(days=1)
        begin = date(2000, 1, 1)
        end = date(2020, 10, 1)
        length = 0
        while begin < end:
            if begin.day == 1 or begin.weekday() == 0:
                length += 2
            else:
                length += 1
            begin += day
        print(length)

    def running2(self):



if __name__ == '__main__':
    arrs = [i for i in range(30)]
    s = ALGORITHMS()
    # s.binary_search(arrs, 30, 0, len(arrs)-1)
    # maxe = s.max_ele(1482, 819); print(maxe)
    # mine = s.min_ele(4, 18)
    # print(mine)
    # s.hanluota(16, "A", 'B', 'C'); s.fp.close()
    # s.node_op()
    s.running()
