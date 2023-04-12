#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int X, Y, prod;
        cin >> X >> Y;
        prod = X * Y;
        cout << prod/100 << endl;

    }
    return 0;
}