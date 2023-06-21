#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, c = 0;
        cin >> N;
        int A[N];
        for (int i = 0; i < N; i++)
        {
            cin >> A[i];
        }
        for (int i = 0; i < N; i++)
        {
            if (A[i] <= 7)
            {
                c += 1;
            }
            if (c == 7)
            {
                cout << i + 1 << endl;
                break;
            }
        }

    }
    return 0;
}