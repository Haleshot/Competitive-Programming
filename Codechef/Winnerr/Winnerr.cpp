#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int Pa, Pb, Qa, Qb, max_P, max_Q;
        cin >> Pa >> Pb >> Qa >> Qb;
        max_P = max(Pa, Pb);
        max_Q = max(Qa, Qb);
        if (max_P > max_Q)
        {
            cout << "Q" << endl;
        }
        else if (max_P < max_Q)
        {
            cout << "P" << endl;
        }
        else
        {
            cout << "TIE" << endl;
        }
        
    }
    return 0;
}