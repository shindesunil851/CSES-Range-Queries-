from sys import stdin, stdout 
import math
 
n, m = map(int, stdin.readline().split())
rooms = list(map(int, stdin.readline().split()))
groups = list(map(int, stdin.readline().split()))
 
 
l = 2**int(math.ceil(math.log(len(rooms),2)))
st = [0] * l + rooms + ([0] * (l - len(rooms)))
for i in range(l-1, 0, -1):
  st[i] = max(st[2*i], st[2*i+1])
 
res = []
for target in groups:
  pos = 1
  while pos <= l-1:
    pos *= 2
    if st[pos] < target:
      pos += 1
 
  pos -= l
  if pos < l-1:
    res.append(pos+1)
    k = pos + l
    st[k] -= target
    k //= 2
    while k >= 1:
      st[k] = max(st[2*k], st[2*k+1])
      k //= 2
  else:
    res.append(0)
 
print(" ".join(str(x) for x in res))
 
 