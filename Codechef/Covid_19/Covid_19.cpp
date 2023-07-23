#include <iostream>
#include <bits/stdc++.h>
#include <list>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        int X[N], c = 0, new_X[N];
        for (int i = 0; i < N; i++)
        {
            cin >> X[i];
        }
        for (int i = 0; i < N; i++)
        {
            if (X[i + 1] - X[i] <= 2)
            {
                c += 1;
            }
            else
            {
                new_X[i] = c;
                c = 1;
            }
        } 
        new_X[sizeof(new_X)] = c;
        cout << (*min_element(new_X, new_X + N)) << endl;

    }
    return 0;
}