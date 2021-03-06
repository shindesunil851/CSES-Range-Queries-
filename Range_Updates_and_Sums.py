func_lazy = lambda (a,b),(c,d): (a*c, b + a*d)
func_data = lambda (a,b),val: a * val + b
 
class LazySegmentTree:
    def __init__(self, data, padding = 0, func=lambda a,b: a + b):
        """initialize the lazy segment tree with data"""
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        
        self.data = [padding] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(1, _size)):
            self.data[i] = self.data[2 * i] + self.data[2 * i + 1]     
        #TODO
        self._lazy = [1,0] * (2 * _size)
 
    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        # TODO
        idx *= 2
        a = self._lazy[idx]
        b = self._lazy[idx + 1]
        if (a,b) != (1,0):
            b >>= 1
            self._lazy[idx] = 1
            self._lazy[idx+1] = 0
            
            self.data[idx] = a * self.data[idx] + b
            self.data[idx + 1] = a * self.data[ idx + 1] + b
            
            idx *= 2
            self._lazy[idx], self._lazy[idx + 1] = func_lazy((a,b), (self._lazy[idx], self._lazy[idx+1]))
            self._lazy[idx + 2], self._lazy[idx + 3] = func_lazy((a,b), (self._lazy[idx + 2], self._lazy[idx + 3]))
    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            # TODO
            #self._push(idx)
            a = self._lazy[2 * idx]
            b = self._lazy[2 * idx + 1]
            self.data[idx] = a * (self.data[2 * idx] + self.data[2 * idx + 1]) + b
            idx >>= 1
 
    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)
 
    def add(self, start, stop, (a,b)):
        """lazily add value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
 
        # Apply all the lazily stored queries
        self._update(start); self._update(stop - 1)
 
        while start < stop:
            if start & 1:
                self.data[start] = a * self.data[start] + b
                self._lazy[2*start],self._lazy[2*start+1] = func_lazy((a,b), (self._lazy[2 * start], self._lazy[2 * start + 1]))
                start += 1
            if stop & 1:
                stop -= 1
                self.data[stop] = a * self.data[stop] + b
                self._lazy[stop * 2], self._lazy[2 * stop + 1] = func_lazy((a,b), (self._lazy[2 * stop], self._lazy[2 * stop + 1]))
            start >>= 1; stop >>= 1; b <<= 1
        
        self._build(start_copy); self._build(stop_copy - 1)
 
    def query(self, start, stop, res = 0):
        """func of data[start, stop)"""
        start += self._size; stop += self._size
 
        # Apply all the lazily stored queries
        self._update(start); self._update(stop - 1)
        while start < stop:
            if start & 1:
                res += self.data[start]
                start += 1
            if stop & 1:
                stop -= 1
                res += self.data[stop]
            start >>= 1; stop >>= 1
        return res
 
    def node_size(self, idx):
        return 1 << self._size.bit_length() - idx.bit_length()
 
def main():
    inp = readnumbers()
    ii = 0
 
    n = inp[ii]
    ii += 1
    q = inp[ii]
    ii += 1
 
    X = inp[ii:ii+n]
    ii += n
 
    seg = LazySegmentTree(X)
 
    for _ in range(q):
        cas = inp[ii]
        ii += 1
        a = inp[ii] - 1
        ii += 1
        b = inp[ii]
        ii += 1
        
        if cas == 1:
            x = inp[ii]
            ii += 1
            seg.add(a, b, (1, x))
        elif cas == 2:
            x = inp[ii]
            ii += 1
            seg.add(a, b, (0,x))
        else:
            cout << seg.query(a,b) << '\n'
 
######## Python 2 and 3 footer by Pajenegod and c1729
 
# Note because cf runs old PyPy3 version which doesn't have the sped up
# unicode strings, PyPy3 strings will many times be slower than pypy2.
# There is a way to get around this by using binary strings in PyPy3
# but its syntax is different which makes it kind of a mess to use.
 
# So on cf, use PyPy2 for best string performance.
 
py2 = round(0.5)
if py2:
    from future_builtins import ascii, filter, hex, map, oct, zip
    range = xrange
 
import os, sys
from io import IOBase, BytesIO
 
BUFSIZE = 8192
class FastIO(BytesIO):
    newlines = 0
 
    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.writable = "x" in file.mode or "w" in file.mode
        self.write = super(FastIO, self).write if self.writable else None
 
    def _fill(self):
        s = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
        self.seek((self.tell(), self.seek(0,2), super(FastIO, self).write(s))[0])
        return s
 
    def read(self):
        while self._fill(): pass
        return super(FastIO,self).read()
 
    def readline(self):
        while self.newlines == 0:
            s = self._fill(); self.newlines = s.count(b"\n") + (not s)
        self.newlines -= 1
        return super(FastIO, self).readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.getvalue())
            self.truncate(0), self.seek(0)
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        if py2:
            self.write = self.buffer.write
            self.read = self.buffer.read
            self.readline = self.buffer.readline
        else:
            self.write = lambda s:self.buffer.write(s.encode('ascii'))
            self.read = lambda:self.buffer.read().decode('ascii')
            self.readline = lambda:self.buffer.readline().decode('ascii')
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline()
 
# Cout implemented in Python
import sys
class ostream:
    def __lshift__(self,a):
        sys.stdout.write(str(a))
        return self
cout = ostream()
endl = '\n'
 
# Read all remaining integers in stdin, type is given by optional argument, this is fast
def readnumbers(zero = 0):
    conv = ord if py2 else lambda x:x
    A = []; numb = zero; sign = 1; i = 0; s = sys.stdin.buffer.read()
    try:
        while True:
            if s[i] >= b'0' [0]:
                numb = 10 * numb + conv(s[i]) - 48
            elif s[i] == b'-' [0]: sign = -1
            elif s[i] != b'\r' [0]:
                A.append(sign*numb)
                numb = zero; sign = 1
            i += 1
    except:pass
    if s and s[-1] >= b'0' [0]:
        A.append(sign*numb)
    return A
 
if __name__== "__main__":
  main()