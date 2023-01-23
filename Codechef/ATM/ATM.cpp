#include <iostream>
using namespace std;
#define MAX 5

int main()
{
    int T = 0, N, K = 0;
    int L[MAX];
    cin >> T;
    while(T--)
    {
        
        cin >> N >> K;
        int L_2[N];

        for(int i = 0; i < N; i++)
        {
            int element;
            cin >> element;
            L[i] = element;
        }

        for(int i = 0; i < N; i++)
        {
            if(L[i] <= K)
            {
                K -= L[i];
                L_2[i] = 1;
            }
            else
            {
                L_2[i] = 0;
            }
        }
        for(int i = 0; i < N; i++)
        {
            cout << L_2[i];
        }
        cout << endl;


    }
    // for(int i = 0; i < N; i++)
    // {
    //     cout << L_2[i];
    // }
    return 0;
}