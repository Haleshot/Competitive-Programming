#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        string J, S;
        cin >> J >> S;
        set<char> m;
        int count = 0;
        for (int i = 0;  i < S.length(); i++)
        {
            char temp = J[i];
            m.insert(temp);
        }
        auto it = J.begin();
        for (auto it = J.begin(); it != J.end(); it++)
        {
            for (int i = 0;  i < S.length(); i++)
            {
                if ((*it) == S[i])
                    count += 1;
            }
        }
    cout << count << endl;

    }
    return 0;
}