#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int A, B, M, t1, t2;
        cin >> A >> B >> M;
        t1 = abs(A - B);
        t2 = abs(M - t1);
        cout << min(t1, t2) << endl;

    }
    return 0;
}