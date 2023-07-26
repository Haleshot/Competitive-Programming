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
            int F_Count = count(inp[i].begin(), inp[i].end(), "F");
            int P_Count = count(inp[i].begin(), inp[i].end(), "P");
            if (F_Count >= X or (F_Count >= (X - 1) and P_Count >= Y))
            {
                cout << "1";
            }
            else
            {
                cout << "0";
            }
        }

    }
    return 0;
}