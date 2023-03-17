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
        cout << (N * 2) + (M * 4) << endl;
    }
    return 0;
}