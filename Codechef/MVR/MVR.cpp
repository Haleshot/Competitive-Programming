#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int A, B, X, Y;
        cin >> A >> B >> X >> Y;
        if (((2 * A) + B) > ((2 * X) + Y))
        {
            cout << "MESSI" << endl;
        }
        else if (((2 * A) + B) < ((2 * X) + Y))
        {
            cout << "RONALDO" << endl;
        }
    }
    return 0;
}