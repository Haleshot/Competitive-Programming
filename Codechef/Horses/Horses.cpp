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
        long int min = 100000;
        sort(S, S + N);
        for (int i = 1; i < N; i++)
        {
            if (S[i] - S[i - 1] < min)
            {
                min = S[i] - S[i - 1];
            }
        }
        cout << min << endl;

    }
    return 0;
}