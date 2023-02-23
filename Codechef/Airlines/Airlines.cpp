#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int X, Y, Z, limit;
        cin >> X >> Y >> Z;
        limit = 10 * X;
        if (limit < Y)
        {
            cout << limit * Z << endl;
        }
        else
        {
            cout << Y * Z << endl;
        }
    }

    return 0;
}