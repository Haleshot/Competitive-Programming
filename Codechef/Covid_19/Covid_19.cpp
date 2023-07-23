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
        vector<int> X(N), new_X(N);  
        for (auto &i : X)
        {
            cin >> i;
        }
        int c = 1, minimum = INT_MAX, maximum = INT_MIN;
        for (int i = 0; i < N - 1; i++)
        {
            if (X[i + 1] - X[i] <= 2)
            {
                ++c;
            }
            else
            {
                minimum = min(minimum, c);
                maximum = min(maximum, c);
                c = 1;
            }
        } 
        minimum = min(minimum, c);
        maximum = min(maximum, c);
        cout << minimum << " " << maximum << endl;        

    }
    return 0;
}