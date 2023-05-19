#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, M;
        cin >> N >> M;
        if (N < M)
        {
            cout << N << endl;
        }
        else
        {
            cout << (N - M + N) << endl;
        }
    }
    return 0;
}