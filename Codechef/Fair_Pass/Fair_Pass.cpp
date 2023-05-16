#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while(T--)
    {
        int N, K, req;
        cin >> N >> K;
        req = N + 1;
        if (K >= req)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    return 0;
}