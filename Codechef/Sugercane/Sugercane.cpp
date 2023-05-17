#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, price;
        cin >> N;
        price = 50 * N;
        cout << int(0.3 * price) << endl;
    }
    return 0;
}