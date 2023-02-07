#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, X, Y;
        cin >> N >> X >> Y;
        string S, a, b;
        cin >> S;
        int L[N], c1 = 0, c2 = 0;
        for (int i = 0; i < N; i++)
        {
            L[i] = S[i];
        }
        if (X < Y)
        {
            sort(L, L + N);
        }
        else
        {
            sort(L, L + N, greater<int>());
        }
        for (int i = 0; i < N; i++)
        {
            cout << L[i];
        }

        for (int i = 0; i < N; i++)
        {
            a = S[i];
            b = S[i + 1];
            if (a == "0" && b == "1")
            {
                c1 += 1;
            }
            else if (a == "1" && b == "0")
            {
                c2 += 1;
            }
            

        }
        cout << (X * c1) + (Y * c2) << endl;
    }

    return 0;
}