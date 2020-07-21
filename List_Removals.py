
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappush, heappop, heapify, nlargest, nsmallest

import os
import sys
sys.setrecursionlimit(1<<30)
from io import BytesIO, IOBase
import math
import bisect
from math import inf
import random
ins = lambda: [int(x) for x in input()]
inp = lambda: int(input())
inps = lambda: [int(x) for x in input().split()]
from fractions import Fraction as F

md=pow(10,9)+7
 
N = 2*(10**5) + 7
bi_tree = [0 for _ in range(N)]

def update(index, value, a):
    while index < len(a):
        bi_tree[index] += value
        index += index & -index


def query(index):

	ans = 0

	while index > 0:
		ans += bi_tree[index]
		index -= index & -index

	return ans


# def build(a, n):
# 	for i in range(n): t[i+n] = 1
 
# 	for i in range(n-1, 0, -1): t[i] = t[i<<1] + t[i<<1|1]


# def query(l, r, n):
# 	l += n
# 	r += n
#   #  l-=1
# 	ret = 0
 
# 	while l < r:
# 		if l&1:
# 			ret += t[l]
# 			l += 1
 
# 		if r&1:
# 			r -= 1
# 			ret += t[r]
 
# 		l >>= 1
# 		r >>= 1
 
# 	return ret
 

# def update(index, val, n):
# 	p = index + n
  
# 	t[p] = val
 
# 	while p > 1:
# 		t[p>>1] = t[p] + t[p^1]
# 		p >>= 1
    
def main():
    n=inp()
    ar=[0]*N
    aa=inps()
    for p,nm in enumerate(aa):
        ar[p+1]=nm
    qu=inps()
    p=[1]*n
    for i in range(n):
        update(i+1,1,ar)
    #build(p,n)
    
    for pts in qu:
        le=0
        re=n+1
        while le+1<re:
            md = le + re >> 1
            if query(md)>=pts:
                re=md
            else:
                le=md
        update(re,-1,ar)
        print(ar[re],end=" ") 



    


BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
# endregion
 
if __name__ == "__main__":
    main()
# import threading,sys
# sys.setrecursionlimit(1000000)
# threading.stack_size(1024000)
# thread=threading.Thread(target=main)
# thread.start()
