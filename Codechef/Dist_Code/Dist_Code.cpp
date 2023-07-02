#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        string S, st;
        int c = 0;
        cin >> S;
        unordered_map<string, int> d;
        
        for (int i = 0; i < S.length() - 1; i++)
        {
            st = S.substr(i, 2);
            d[S.substr(i, 2)]++;
        }
        for (auto x : d)
        cout << x.first << " " << x.second << endl;
    }
    return 0;
}

