#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int X, P, Q;
        cin >> X >> P >> Q;
        cout << ((P - Q) * X) << endl;
    }
    return 0;
}