#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        long long D, d, P, Q;
        cin >> D >> d >> P >> Q;
        long res = ((d * (D / d) * (2 * P + ((D / d) - 1) * Q)) / 2) + ((D % d) * (P + (D / d) * Q));
        cout << res << endl;
    }
    return 0;
}