#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, M, X, Y;
        cin >> N >> M >> X >> Y;
        string inp[N];
        for (int i = 0; i < N; i++)
        {
            cin >> inp[i];
        }
        for (int i = 0; i < N; i++)
        {
            int F_Count = count(inp[i].begin(), inp[i].end(), "F");
            int P_Count = count(inp[i].begin(), inp[i].end(), "P");
        }
    }
    return 0;
}