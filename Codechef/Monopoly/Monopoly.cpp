#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int R1, R2, R3;
        cin >> R1 >> R2 >> R3;
        if (R1 > (R2 + R3))
        {
            cout << "YES" << endl;
        }
        else if (R2 > (R1 + R3))
        {
            cout << "YES" << endl;
        }
        else if (R3 > (R1 + R2))
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }

    return 0;
}