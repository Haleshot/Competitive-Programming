#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int A, B, C, D;
        cin >> A >> B >> C >> D;
        A -= C;
        B -= D;
        if (A < B)
        {
            cout << "First" << endl;
        }
        else if (B < A)
        {
            cout << "Second" << endl;
        }
        else
        {
            cout << "Any" << endl;
        }
    }
    return 0;
}