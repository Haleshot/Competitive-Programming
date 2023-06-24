#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int R;
        cin >> R;
        R *= 1000;
        R /= 2;
        cout << R/5 << endl;
    }
    return 0;
}