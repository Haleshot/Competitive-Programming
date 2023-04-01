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
        sort(l, l + 4);
        cout << l[3] << endl;

        
    }
    return 0;
}