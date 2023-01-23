#include <iostream>
using namespace std;
#define MAX 5

int main()
{
    int T = 0, N, K = 0;
    int L[MAX], L_2[MAX];
    cin >> T;
    while(T--)
    {
        cin >> N >> K;

        for(int i = 0; i <= N; i++)
        {
            int element;
            cin >> element;
            L[i] = element;
        }
        for(int i = 0; i < N; i++)
        {
            if(L[i] <= K)
            {
                K -= i;
                L_2[i] = 1;
            }
            else
            {
                L_2[i] = 0;
            }
        }


    }
    return 0;
}