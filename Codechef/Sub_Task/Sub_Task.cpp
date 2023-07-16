#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, M, K;
        cin >> N >> M >> K;
        int A[N];
        int one_count = 0;
        for (int i = 0; i < N; i++)
        {
            cin >> A[i];
        }
        for (int i = 0; i < N; i++)
        {
            if (A[i] == 1)
                one_count += 1;       
            else
                break; 
        }
        if (one_count == N)
            cout << 100 << endl;
        else if (one_count >= M)
            cout << K << endl;
        else
            cout << 0 << endl;
    }
    return 0;
}