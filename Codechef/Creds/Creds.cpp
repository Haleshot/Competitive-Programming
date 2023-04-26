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
        cout << (4 * X) + (2 * Y) << endl;
    }
    return 0;
}