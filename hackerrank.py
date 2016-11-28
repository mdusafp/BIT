#!/usr/bin/py
 
class BinaryIndexedTree():
    def __init__(self, size):
        self.sz = size
        self.tree = [0] * size

    def update(self, index, value):
        while (index < self.sz):
               self.tree[index] += value
               index += (index & -index)

    def read(self, index):
        sum = 0
        while (index > 0):
            sum += self.tree[index]
            index -= (index & -index)
        return sum
 
if __name__ == '__main__':
    tests = input()
    for _ in range(tests):
        n = input()
        array = map(int, raw_input().split())
        count = 0
        bit = BinaryIndexedTree(10**1+1)
        for val in reversed(array):
            bit.update(val, 1)
            count += bit.read(val-1)
        print count