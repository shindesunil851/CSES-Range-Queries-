#include <bits/stdc++.h>
 
using namespace std;
 
#define int long long
 
int n;
vector<vector<int>> t;
 
void upd(int a, int b, int d) {
    for (int i = a; i <= n; i = (i | (i + 1))) {
        for (int j = b; j <= n; j = (j | (j + 1)))
            t[i][j]+=d;
    }
    return;
}
 
int get(int a, int b) {
    int ans = 0;
    for (int i = a; i >= 0; i = (i & (i + 1)) - 1) {
        for (int j = b; j >= 0; j = (j & (j + 1)) - 1) ans += t[i][j];
    }
    return ans;
}
 
int get(int a, int b, int c, int d) {
    return get(c, d) - get(a - 1, d) - get(c, b - 1) + get(a - 1, b - 1);
}
 
int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n; int q; cin >> q;
    t.resize(n, vector<int>(n));
    vector<vector<char>> mp(n, vector<char>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> mp[i][j];
            if (mp[i][j] == '*') {
                upd(i, j, 1);
            }
        }
    }
    for (; q > 0; q--) {
        int t; cin >> t;
        if (t == 1) {
            int a, b; cin >> a >> b; a--; b--;
            if (mp[a][b] == '*') {
                mp[a][b] = '.';
                upd(a, b, -1);
            }
            else {
                mp[a][b] = '*';
                upd(a, b, 1);
            }
        }
        else {
            int a, b, c, d; cin >> a >> b >> c >> d;
            a--; b--; c--; d--;
            cout << get(a, b, c, d) << endl;
        }
    }
    return 0;
}