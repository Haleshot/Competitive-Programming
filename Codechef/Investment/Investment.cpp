#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int X, Y;
        cin >> X >> Y;
        if (X >= 2 * Y)
        {
            cout << "YES" << endl;
        }
    }
    return 0;
}