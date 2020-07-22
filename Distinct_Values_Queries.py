
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

md=pow(10,7)+1


class Q:
    def __init__(self,l,r,i):
        self.l=l
        self.r=r
        self.i=i
        

def main():
    n,m=inps()


    blk=sqrt(n)
    a=inps()
    
    mp=defaultdict(int)
    cmpr=1
    for i,nm in enumerate(a):
        if mp[nm]==0:
            a[i]=cmpr
            mp[nm]=cmpr
            cmpr+=1

        else:
            a[i]=mp[nm]


    q=[]
    for i in range(m):
        l,r=inps()
        l-=1
        r-=1
        ob=Q(l,r,i)
        q.append(ob) 
    q.sort(key=lambda x: (x.l//blk,x.r//blk))

    ml=0
    mr=-1
    cnt=0
    ans=[0]*(m+1)
    dc=[0]*(max(a)+1)
    for j in range(m):
        L=q[j].l
        R=q[j].r
        qnm=q[j].i

        while mr<R:
            mr+=1
            dc[a[mr]]+=1
            if dc[a[mr]]==1:
                cnt+=1
            
        
        while ml>L:
            ml-=1
            dc[a[ml]]+=1
            if dc[a[ml]]==1:
                cnt+=1
            
        
        while mr>R:
            dc[a[mr]]-=1
            if  dc[a[mr]]==0:
                cnt-=1
            mr-=1
        
        while ml<L:
            dc[a[ml]]-=1
            if dc[a[ml]]==0:
                cnt-=1
            ml+=1

        ans[qnm]=cnt
    for nm in ans[:-1]:
        print(nm)

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
