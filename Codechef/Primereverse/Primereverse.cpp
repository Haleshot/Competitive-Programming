#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int Count_Freq(string X, string Y, int limit)
{
    map<int, int> cf;
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
