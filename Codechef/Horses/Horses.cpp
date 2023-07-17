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
        long long diff = 100000;
        sort(S, S + N);
        for (int i = 0; i < N - 1; i++)
        {
            if (S[i + 1] - S[i] < diff)
            {
                diff = S[i + 1] - S[i];
            }
        }
        cout << diff << endl;

    }
    return 0;
}