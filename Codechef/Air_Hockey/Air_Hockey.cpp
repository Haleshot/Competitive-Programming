#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int A, B;
        cin >> A >> B;
        A = 7 - A;
        B = 7 - B;
        cout << min(A, B) << endl;
    }
    return 0;
}