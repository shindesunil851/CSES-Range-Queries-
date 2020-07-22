#include <bits/stdc++.h>
 
using namespace std;
 
#pragma GCC optimize ("O3")
#pragma GCC target ("sse4")
#define int long long
 
const int maxn = 200010, INF = -1e15;
struct dta {
    int best, total, pre, suf;
};
dta tree[4 * maxn];
int ar[maxn];
 
dta doit(dta a, dta b) {
    dta d = {0, 0, 0, 0};
    d.total = a.total + b.total;
    d.suf = max(b.suf, a.suf + b.total);
    d.pre = max(a.pre , a.total + b.pre);
    d.best = max({d.pre, d.suf, a.best, b.best, a.suf + b.pre});
    return d;
}
 
void build(int start, int end, int index = 1) {
    if (start == end) {
        tree[index].best = ar[start];
        tree[index].pre = ar[start];
        tree[index].total = ar[start];
        tree[index].suf = ar[start];
        return;
    }
    int mid = (start + end) >> 1;
    build(start, mid, 2 * index);
    build(mid + 1, end, 2 * index + 1);
    tree[index] = doit(tree[2 * index], tree[2 * index + 1]);
}
 
dta queryTree(int start, int end, int l, int r, int index = 1) {
#warning :- Dont forget to change the return type of this shit
    if (r < start or l > end) 
    {
        return {INF, INF, INF, INF};
    }
    if (l <= start and r >= end)
        return tree[index];
    int mid = start + end >> 1;
    return (doit(queryTree(start, mid, l, r, 2 * index), queryTree(mid + 1, end, l, r, 2 * index + 1)));

}
 
void update(int start, int end, int x, int val, int index) {
    if (x < start or x > end)
        return;
 
    if (start == end) {
        tree[index].pre = val;
        tree[index].best = val;
        tree[index].suf = val;
        tree[index].total = val;
        return;
    }
 
    int mid = start + end >> 1;
    update(start, mid, x, val, 2 * index);
    update(mid + 1, end, x, val, 2 * index + 1);
    tree[index] = doit(tree[2 * index], tree[2 * index + 1]);
}
 
int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int n, m;
    cin >> n >> m;
 
    for (int i = 0; i < n; ++i) {
        cin >> ar[i];
    }
 
    build(0, n - 1);
    while (m--) {
        int a, b;
        cin >> a >> b;
 
        update(0, n - 1, a - 1, b, 1);
        cout << max(0ll, queryTree(0, n - 1, 0, n - 1, 1).best) << endl;
    }
    return 0;
}