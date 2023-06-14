#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int P, Q, points;
        cin >> P >> Q;
        points = P + Q;
        if (((P + Q) % 4 == 0) || ((P + Q) % 4 == 1))
        {
            cout << "ALICE" << endl;
        }
        

    }
    return 0;
}