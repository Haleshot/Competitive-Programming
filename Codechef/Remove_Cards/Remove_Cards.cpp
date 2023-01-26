#include <iostream>
#include <bits/stdc++.h>
#define MAX 100
using namespace std;

int main()
{
    int T;
    cin >> T;
    while(T)
    {
        T -= 1;
        int N, *l;
        vector<bool> visited(N, false);
        cin >> N;
        l = new int [N];

        for(int i = 0;i < N; i ++)
        {
            int a;
            cin >> a;
            l[i] = a;
        }
        for(int i = 0; i < N; i ++)
        {
            if(visited[i] = true)
            {
                continue;
            }

            int count = 1;
            for (int j = i + 1; j < N; j++)
            {
                if(l[i] == l[j])
                {
                    visited[i] = true;
                    count += 1;
                }
            }
            cout << l[i] << count << endl;
        }


    }

    return 0;

}