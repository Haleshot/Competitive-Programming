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

    }

    return 0;
}
