#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, index_1, index_N;
        cin >> N;
        int P[N];
        for (int i = 0; i < N; i++)
        {
            cin >> P[i];
        }
        index_1 = find(P, P + N, 1) - P;
        index_N = find(P, P + N, N) - P;
        if (index_1 < index_N)
        {
            cout << index_1 + N - 1 - index_N << endl;
        }
        else
        {
            cout << index_1 + N - 2 - index_N << endl;
        }
    }
    return 0; 
}
