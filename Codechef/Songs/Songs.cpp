#include <iostream>
#include <cmath>
using namespace std;


int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, X, total;
        cin >> N >> X;
        total = X * 3;
        cout << floor(N/total) << endl;
    }
    return 0;
}