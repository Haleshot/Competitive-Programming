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
        for (int i = 1; i < 100; i++)
        {
            if (A % i != 0 && B % i != 0 && C % i != 0)
            {
                cout << i << endl;
                break;
            }
        }
    }
    return 0;
}