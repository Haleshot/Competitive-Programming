#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

int Count_Freq(string word, int limit)
{
    unordered_map<int, int> cf;
    int l[limit];

    for (int i = 0; i < limit; i ++)
        {
            cf[word[i]]++;
        }

        int j = 0;
        for (auto i : cf) // Traversing the Unordered map
        {
            l[j] = i.second;
            j += 1;
        }
        
        int count = 0;
        for (int i = 0; i < limit; i++)
        {
            if(l[i] % 2 == 0)
            {
                count++;
            }

            else
            {
                count = 0;
                break;
            }
        }

        if (count > 0)
        {
            return true;
        }

        else
        {
            return false;
        }

}


int main()
{

    int T;
    cin >> T;
    while(T--)
    {
        int N;        
        string S = "";
        cin >> N;
        cin >> S;

        if(S.length() == N)
        {
            int result = Count_Freq(S, N);
            if (result)
            {
                cout << "YES" << endl;
            }
            else
            {
                cout << "NO" << endl;
            }

        }

    }

    return 0;
}