#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int X, Y, middle;
        cin >> X >> Y;
        middle = (X + Y)/2;
        cout << max(abs(middle - X), abs(middle - Y)) << endl;
    }
    return 0;
}