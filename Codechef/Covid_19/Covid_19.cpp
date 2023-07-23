#include <iostream>
#include <bits/stdc++.h>
#include <vector>
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
        vector<int> X(N);  
        int c = 1, minimum = INT_MAX, maximum = INT_MIN;
        for (auto &i : X)
        {
            cin >> i;
        }
        for (int i = 0; i < N - 1; ++i)
        {
            if (abs(X[i + 1] - X[i] <= 2))
            {
                ++c;
            }
            else
            {
                minimum = min(minimum, c);
                maximum = max(maximum, c);
                c = 1;
            }
        } 
        minimum = min(minimum, c);
        maximum = max(maximum, c);
        cout << minimum << " " << maximum << endl;        

    }
    return 0;
}