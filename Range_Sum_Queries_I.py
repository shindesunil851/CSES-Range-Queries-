from heapq import *
from collections import *
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

def build(sg,a,nd,low,high):
    if low>high:
        return 0
    if low==high:
        sg[nd]=a[low]
        return sg[nd]
    
    md=low+(high-low)//2
    sg[nd]=build(sg,a,2*nd+1,low,md)+build(sg,a,2*nd+2,md+1,high)
    return sg[nd]

def getv(sg,a,nd,low,high,l,r):
    if low>r or high<l:
        return 0
    if l<=low and high<=r:
        return sg[nd]
    m=low+(high-low)//2
    return getv(sg,a,2*nd+1,low,m,l,r)+getv(sg,a,2*nd+2,m+1,high,l,r)

def main():
    n,q=inps()
    a=inps()
#    sg=[0]*4*n
#    build(sg,a,0,0,n-1)
    pr=[0]*(n+1)

    pr[0]=a[0]
    for i in range(1,n):
        pr[i]+=pr[i-1]+a[i]
    for _ in range(q):
        l,r=inps()
        l-=1
        r-=1
        #print(getv(sg,a,0,0,n-1,l,r))
        if not l:
            print(pr[r])
        else:
            print(pr[r]-pr[l-1])


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