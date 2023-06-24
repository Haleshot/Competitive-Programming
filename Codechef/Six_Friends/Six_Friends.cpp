#include <iostream>
using namespace std;

int main()
{
    int T;
    cin  >> T;
    while (T--)
    {
        int X, Y;
        cin >> X >> Y;
        cout << min((3 * X), (2 * Y)) << endl;
    }
    
    return 0;
}