#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, M;
        long long int total = 0;
        cin >> N >> M;
        if ((total) % 2 == 0)
        {
            cout << "1/2" << endl;
        }
        else
        {
            cout << (total) / 2 << "/" << total << endl;
        }
    }
    return 0;
}