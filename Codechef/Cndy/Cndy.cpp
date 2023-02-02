#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int Count_Freq(int X[], int limit)
{
    map<int, int> cf;

    for (int i = 0; i < limit; i ++)
    {
        cf[X[i]]++;
    }

    // int j = cf.size();
    // int l[j];
    // int k = 0;    
    // for (auto i : cf) // Traversing the Unordered map
    // {
    //     if(k < j)
    //     {
    //         l[k] = i.second;
    //         k += 1;
    //     }
        
    // }

    // int c = 0;
    // for (int i = 0; i < limit; i ++)
    // {
    //     if (l[i] > 2)
    //     {
    //         c += 1;
    //         break;
    //     }
    // }

    int c = 0;
    for (auto i : cf) // Traversing the Unordered map
    {
        if (i.second > 2)
        {
            c += 1;
            break;
        }
        
    }

    if (c > 0)
    {
        return false;
    }
    else
    {
        return true;
    }

}

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        int A[2 * N];
        for (int i = 0; i < 2 * N; i ++)
        {
            cin >> A[i];
        }

        int result = Count_Freq(A, 2 * N);

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