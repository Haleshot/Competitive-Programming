#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int X, ten;
        cin >> X;
        ten = 0.1 * X;
        cout << max(ten, 100) << endl;
    }
    return 0;
}