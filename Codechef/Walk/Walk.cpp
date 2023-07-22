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
        int W[N];
        for (int i = 0; i < N; i++)
        {
            cin >> W[i];
        }
        for (int i = 0; i < N; i++)
        {
            W[i] += i;
        }
        cout << *max_element(W, W + N) << endl;
    }
    return 0;
}