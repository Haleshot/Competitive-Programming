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
        int S[N];
        for (int i = 0; i < N; i++)
        {
            cin >> S[i];
        }
        int diff = 100000;
        sort(S, S + N);
        for (int i = 1; i < N; i++)
        {
            if (S[i] - S[i - 1] < diff)
            {
                diff = S[i] - S[i - 1];
            }
        }
        cout << diff << endl;

    }
    return 0;
}