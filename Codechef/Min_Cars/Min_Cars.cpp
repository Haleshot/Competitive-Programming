#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int X;
        cin >> X;
        cout << ceil(X/4) << endl;
    }
    return 0;
}