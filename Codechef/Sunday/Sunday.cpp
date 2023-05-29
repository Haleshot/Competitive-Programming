#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        int A[N];
        for (int i = 0;i < N; i++)
        {
            cin >> A[i];
        }
        int c = 0;
        for (int i = 0; i < N; i++)
        {
            if (A[i] == 6 || A[i] == 7 || A[i] == 13 || A[i] == 14 || A[i] == 20 || A[i] == 21 || A[i] == 27 || A[i] == 28)
            {
                c += 1;
            }
        }
        cout << (8 + (N - c)) << endl;
        
    }
    return 0;
}