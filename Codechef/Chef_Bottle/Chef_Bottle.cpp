#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, X, K, num;
        cin >> N >> X >> K;
        if (X <= K)
        {
            num = K/X;
            if (num >= N)
            {
                cout << N << endl;
            }
            else
            cout << num << endl;
        }
        else
        {
            cout << K/X << endl;
        }
    }
    return 0;
}