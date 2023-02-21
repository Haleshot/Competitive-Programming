#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int X, Y, Z;
        cin >> X >> Y >> Z;
        X = 400/X;
        Y = 400/Y;
        Z = 400/Z;
        if (X > Y && X > Z)
        {
            cout << "ALICE" << endl;
        }
        else if (Y > X && Y > Z)
        {
            cout << "BOB" << endl;
        }
        else if (Z > X && Z > Y)
        {
            cout << "CHARLIE" << endl;
        }
    }
    return 0;
}