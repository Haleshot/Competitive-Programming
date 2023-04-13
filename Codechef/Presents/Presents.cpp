#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, temp;
        cin >> N;
        if (N % 5 == 0)
        {
            temp = int(N / 5);
            cout << 4 * temp << endl;
        }
        else
        {
            temp = N / 5;
            cout << N - temp << endl;
        }
    }
    return 0;
}