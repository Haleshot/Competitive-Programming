#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int A, B, C;
        cin >> A >> B >> C;
        if (((A + B) %2 == 1) || ((A + C) % 2 == 1) || ((B + C) % 2 == 1))
        {
            cout << "PASS" << endl;
        }
        else
        {
            cout << "FAIL" << endl;
        }
    }
    return 0;
}