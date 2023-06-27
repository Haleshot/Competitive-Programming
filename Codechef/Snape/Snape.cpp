#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int B, LS;
        cin >> B >> LS;
        cout << setprecision(2) << sqrt(LS*LS - B*B) << " " << sqrt(LS*LS + B*B) << endl;
    }
    return 0;
}