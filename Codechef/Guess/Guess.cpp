#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        long long int N, M;
        cin >> N >> M;
        long long int total = N * M;
        
        if (N == 1 && M == 1)
            cout << "0/1" << endl;

        else if (N % 2 == 0 || M % 2 == 0)
        {
            cout << "1/2" << endl;
        }

        else
        {
            long long int temp = total / 2;
            cout << temp << "/" << total << endl;
        }
    }
    return 0;
}