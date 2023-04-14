#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        float X, Y;
        cin >> X >> Y;
        X = ceil(X/10);
        Y = ceil(Y/10);
        cout << abs(X - Y) << endl;
    }
    return 0;
}