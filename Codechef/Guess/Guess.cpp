#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, M;
        cin >> N >> M;
        if ((N * M) % 2 == 0)
        {
            cout << "1/2" << endl;
        }
        else
        {
            cout << (N/2) << "/" << (N) << endl;
        }
    }
    return 0;
}