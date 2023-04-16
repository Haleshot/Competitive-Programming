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
        if (X % 3 == 0)
        {
            cout << "NORMAL" << endl;
        }
        else if (X % 3 == 1)
        {
            cout << "HUGE" << endl;
        }
        else
        {
            cout << "SMALL" << endl;
        }
    }
    return 0;
}