#include <iostream>
using namespace std;


int main()
{
    int T;
    cin >> T;
    
    while (T--)
    {
        int S, X, Y, Z, remain;
        cin >> S >> X >> Y >> Z;
        if (Z <= remain)
        {
            cout << "0" << endl;
        }
        else if (S >= (X + Z) || Z >= (Y + Z))
        {
            cout << "1" << endl;
        }
        else
        {
            cout << "2" << endl;
        }

    }
    return 0;
}