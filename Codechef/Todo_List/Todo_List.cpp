#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, c = 0;
        cin >> N;
        int l[N];
        for(int i = 0; i <= N;i ++)
        {
            cin >> l[i];
        }
        for (int i = 0;i < N; i++)
        {
            if (l[i] >= 1000)
            {
                c += 1;
            }
        }
        cout << c << endl;
    }
    return 0;
}