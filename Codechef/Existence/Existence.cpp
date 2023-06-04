#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int X, Y, LHS, RHS;
        cin  >> X >> Y;
        LHS = pow(X, 4) + (4 * pow(Y, 2));
        RHS = 4 * (pow(X, 2) * Y);
        if (LHS == RHS)
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