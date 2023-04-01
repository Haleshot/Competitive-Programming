#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, Na, Nb, Nc, Nd;
        cin >> N >> Na >> Nb >> Nc >> Nd;
        int l[] = {Na, Nb, Nc, Nd};
        sort(l);
        cout << l[0] << endl;

        
    }
    return 0;
}