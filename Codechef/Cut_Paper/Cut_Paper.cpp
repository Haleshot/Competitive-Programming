#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, K;
        cin >> N >> K;
        cout << (N/K) * (N/K) << endl;
    }
    return 0;
}