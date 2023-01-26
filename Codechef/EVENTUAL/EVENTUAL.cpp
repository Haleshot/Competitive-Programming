#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

int Count_Freq(int l[], int limit)
{
    unordered_map<int, int> cf;

    for(int i = 0; i < limit; i ++)
        {
            cf[l[i]]++;
        }

        auto pr = max_element(cf.begin(), cf.end(), [](const auto &x, const auto &y) {
                    return x.second < y.second;
                });
 
    return pr->first;


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


        }



    }



    return 0;
}