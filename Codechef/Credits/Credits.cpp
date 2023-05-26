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
        if (X > 65)
        {
            cout << "OVERLOAD" << endl;
        }
        if (X < 35)
        {
            cout << "UNDERLOAD" << endl;
        }
        else
        {
            cout << "NORMAL" << endl;
        }
    }
    return 0;
}