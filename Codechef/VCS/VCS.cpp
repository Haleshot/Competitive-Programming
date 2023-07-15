#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, M, K, first = 0, second = 0;
        cin >> N >> M >> K;
        int A[M], B[K];
        for (int i = 0; i < M; i++)
        {
            cin >> A[i];
        }
        for (int i = 0; i < K; i++)
        {
            cin >> B[i];
        }
        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < K; j++)
            {
                if (A[i] == B[j])
                {
                    first += 1;
                }
            }
        }
       
        cout << first << " " << N - (M + K - first) << endl;


    }
    return 0;
}