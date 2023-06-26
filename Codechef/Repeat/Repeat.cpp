#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, K, S, c = 0;
        cin >> N >> K >> S;
        for (int i = 0; i < 2 * N + 1; i++)
        {
            if (i % 2 == 1)
            {
                c += i;
            }
        }    
        cout << (int((S - c)/(K - 1))) << endl;
    }
    return 0;
}