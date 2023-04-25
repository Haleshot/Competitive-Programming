#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int X, Y, Z, t;
        cin >> X >> Y >> Z;
        t = Y/X;
        if (Z > t)
        {
            cout << Z - t << endl;
        }
        else
        {
            cout << "0" << endl;
        }
    }
    return 0;
}