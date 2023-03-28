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
        if (Y >= 0.5 * X)
        {
            cout << "YES" << endl;
        }
    }
    return 0;
}