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
        if (X <= Y)
        {
            cout << Z << endl;
        }
    }
    return 0;
}