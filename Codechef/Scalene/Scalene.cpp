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
        if (A != B && B != C && A != C)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }

    }
    return 0;
}
 