#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        float H, X, Y, attacks;
        cin >> H >> X >> Y;
        H -= Y;
        cout << ceil((H/X)) + 1 << endl;
    }
    return 0;
}