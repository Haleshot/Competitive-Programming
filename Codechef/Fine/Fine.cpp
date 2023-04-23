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
    }
    return 0;
}