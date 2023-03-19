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
        cout << (X * 4) + Y << endl;
    }
    return 0;
}