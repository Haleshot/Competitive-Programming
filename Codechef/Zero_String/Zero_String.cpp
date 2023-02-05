#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        string S;
        char x;
        cin >> N >> S;
        int c1 = 0, c2 = 0;
        for (int i = 0; i < S.length(); i++)
        {
            x = S[i];
            if (x == '0')
            {
                c1 += 1;
            }
        }
        c2 = N - c1;
        if (c1 >= c2)
        {
            cout << c2 << endl;
        }
        
        else
        {
            cout << c1 + 1 << endl;
        }
    }
    return 0;
}