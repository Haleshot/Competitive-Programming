#include <iostream>
#include <numeric>   
using namespace std;

int arraySum(int a[], int n)
{
    int initial_sum = 0;
    return accumulate(a, a + n, initial_sum);
}

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, K, V;
        cin >> N >> K >> V;
        int A[N];
        for (int i = 0; i < N; i++)
        {
            cin >> A[i];
        }
        int result;
        int n = sizeof(A)/sizeof(A[0]);
        result = float((V * (N + K)) - arraySum(A, n));
        if (result % K == 0 && result > 0)
        {
            cout << int(result)/K << endl;
        }
        else
        {
            cout << -1 << endl;
        }

    }
    return 0;
}