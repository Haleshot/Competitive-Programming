#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        float A, X, B, Y;
        cin >> A >> X >> B >> Y;
        if ((A/X) > (B/Y))
        {
            cout << "ALICE" << endl;
        }
        else if (((A/X) < (B/Y)))
        {
            cout << "BOB" << endl;
        }
        else
        {
            cout << "EQUAL" << endl;
        }
    }

    return 0;
}