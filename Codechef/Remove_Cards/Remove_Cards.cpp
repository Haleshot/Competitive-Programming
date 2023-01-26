#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int Count_Freq(int l[], int limit)
{
    unordered_map<int, int> cf;

    for (int i = 0; i < limit; i ++)
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
        int N, *l, max_freq;
        cin >> N;
        l = new int [N];

        for (int i = 0;i < N; i ++)
        {
            int a;
            cin >> a;
            l[i] = a;
        }
        
        max_freq = Count_Freq(l, N);
        int c = 0;
        for (int i = 0; i < N; i++)
        {
            if(l[i] != max_freq)
            {
                c++;
            }

        }

        cout << c << endl;
        


    }

    return 0;

}