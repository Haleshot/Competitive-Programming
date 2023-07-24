#include <iostream>
#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        vector <int> m(1440, 0);
        for (int i = 0; i < 2 * N; i++)
        {
            int temp;
            cin >> temp;
            m[temp]++;
        }
        sort(m.begin(), m.end(), greater<int>());
        cout << m[0] << endl;

    }
    return 0;
}