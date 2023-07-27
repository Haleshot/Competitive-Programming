#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while ( (T--))
    {
        int A, B, P, Q;
        cin >> A >> B >> P >> Q;
        if (((A == P) && (B == Q)))
            cout << 0 << endl;
        else if ((A + B) % 2 == (P + Q) % 2)
            cout << 2 << endl;
    }
    
    return 0;
}