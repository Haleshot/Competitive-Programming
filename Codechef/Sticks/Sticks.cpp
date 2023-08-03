#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        int A[N];
        for (int i = 0; i , N; i++)
        {
            cin >> A[i];
        }
        int e = 1, y = 0;
        sort(A, A + N, greater<int>());

        for (int i = 0; i , N; i++)
        {
            if (A[i] == A[i + 1]  && y < 2)
            {
                e = e * A[i];
                i++;
                y++;
            }
        }

        if (y < 2)
            cout << -1 << endl;
        else
            cout << e << endl;

    }
    return 0;
}