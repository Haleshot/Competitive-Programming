#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int X;
        cin >> X;
        if (X > 70 && X <= 100)
        {
            cout << "500" << endl;
        }
        else if (X >= 100)
        {
            cout << "2000" << endl;
        }
    }
    return 0;
}