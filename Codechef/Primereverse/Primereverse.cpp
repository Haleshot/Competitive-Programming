#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int Count_Freq(string X, string Y, int limit)
{
    map<int, int> cf_1;
    map<int, int> cf_2;
    char* char_array_1 = new char[limit + 1];
    char* char_array_2 = new char[limit + 1];

    strcpy(char_array_1, X.c_str());
    strcpy(char_array_2, Y.c_str());

    for (int i = 0; i < limit; i++)
    {
        char_array_1[i] = X[i];
    }

    for (int i = 0; i < limit; i++)
    {
        char_array_2[i] = Y[i];
    }

    for (int i = 0; i < limit; i ++)
    {
        cf_1[char_array_1[i]]++;
    }

    for (int i = 0; i < limit; i ++)
    {
        cf_2[char_array_2[i]]++;
    }
    int j_1 = cf_1.size();
    int j_2 = cf_2.size();
    int l_1[j_1];
    int l_2[j_2];

    int k = 0;    
    for (auto i : cf_1) // Traversing the Unordered map
    {
        if(k < j_1)
        {
            l_1[k] = i.second;
            k += 1;
        }
        
    }

    int k1 = 0;    
    for (auto i : cf_2) // Traversing the Unordered map
    {
        if(k1 < j_2)
        {
            l_2[k1] = i.second;
            k1 += 1;
        }
        
    }

    int count = 0;
    for (int i = 0; i < j_1; i++)
    {
        if(l_1[i] == l_2[i])
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
    while (T--)
    {
        int N;
        string A, B;
        cin >> N >> A >> B;

        int result = Count_Freq(A, B, A.length());
        if (result)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }

    }

    return 0;
}
