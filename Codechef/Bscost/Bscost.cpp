#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;


int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, X, Y;
        cin >> N >> X >> Y;
        string S;
        cin >> S;
        int L[N];
        for (int i = 0; i < N; i++)
        {
            L[i] =  S[i] - '0';
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
            cout << L[i] << endl;
        }

        int c1 = 0, c2 = 0;
        for (int i = 0; i < N; i++)
        {
            if (L[i] == 0 && L[i + 1] == 1)
            {
                c1 += 1;
            }
            else if (L[i] == 1 && L[i + 1] == 0)
            {
                c2 += 1;
            }

        }
        cout << c1 << ", " << c2 << endl;
        cout << (X * c1) + (Y * c2) << endl;
    }

    return 0;
}