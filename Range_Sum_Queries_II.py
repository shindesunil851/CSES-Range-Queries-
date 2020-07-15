from sys import stdin, stdout
 
N = 2*(10**5) + 7
t = [0 for _ in range(2*N)]
 
def build(a, n):
	for i in range(n): t[i+n] = a[i]
 
	for i in range(n-1, 0, -1): t[i] = t[i<<1] + t[i<<1|1]
 
def query(l, r, n):
	l += n
	r += n
 
	ret = 0
 
	while l < r:
		if l&1:
			ret += t[l]
			l += 1
 
		if r&1:
			r -= 1
			ret += t[r]
 
		l >>= 1
		r >>= 1
 
	return ret
 
def update(index, val, n):
	p = index + n
 
	t[p] = val
 
	while p > 1:
		t[p>>1] = t[p] + t[p^1]
		p >>= 1
 
def main():
	n, q = list(map(int, stdin.readline().strip().split()))
	a = list(map(int, stdin.readline().strip().split()))
 
	build(a, n)
 
	for _ in range(q):
		t, a, b = list(map(int, stdin.readline().strip().split()))
 
		if t == 1:
			a -= 1
 
			update(a, b, n)
 
		else:
			stdout.write(str(query(a-1, b, n)) + "\n")
 
if __name__ == "__main__": main()