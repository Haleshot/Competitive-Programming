#include <iostream>
#include <cstring>
#include <bits/stdc++.h>
#include <string>
using namespace std;

int Count_Freq(string word, int limit)
{
    unordered_map<int, int> cf;
    int l[limit];
    char* char_array = new char[limit + 1];
    strcpy(char_array, word.c_str());


    for (int i = 0; i < limit; i ++)
        {
            cf[char_array[i]]++;
        }

        int j = 0;
        for (auto i : cf) // Traversing the Unordered map
        {
            l[j] = i.second;
            j += 1;
        }
        
        for (int i = 0; i < limit; i ++) // Traversing the Unordered map
        {
            cout << l[i] << endl << endl;
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
            int result = Count_Freq(S, S.length());
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