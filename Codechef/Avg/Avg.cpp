#include <iostream>
#include <numeric>   
using namespace std;

int arraySum(int a[], int n)
{
    int initial_sum = 0;
    return accumulate(a, a+n, initial_sum);
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
        float result;
        int n = sizeof(a)/sizeof(a[0]);
        result = ((V * (N + K)) - arraySum(A, n))/K;
        

    }
    return 0;
}