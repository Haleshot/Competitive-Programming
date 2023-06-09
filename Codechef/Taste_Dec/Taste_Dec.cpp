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
        if ((2 * X) > (5 * Y))
        {
            cout << "Chocolate" << endl;
        }
        else if ((2 * X) < (5 * Y))
        {
            cout << "Candy" << endl;
        }
        else
        {
            cout << "Either" << endl;
        }
    }
    return 0;
}