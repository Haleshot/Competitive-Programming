#include <iostream>
using namespace std;

int main()
{
    int A, B, C, X;
    cin >> A >> B >> C >> X;
    if (X == A || X == B || X == C)
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }

    return 0;
}