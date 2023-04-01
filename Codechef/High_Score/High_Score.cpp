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
        int n = sizeof(l) / sizeof(l[0]);
        sort(l, l + n);
        cout << l[0] << endl;

        
    }
    return 0;
}