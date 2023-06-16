#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int C;
        cin >> C;
        if (C > 20)
        {
            cout << "HOT" << endl;
        }
        else
        {
            cout << "COLD" << endl;
        }
    }
    return 0;
}