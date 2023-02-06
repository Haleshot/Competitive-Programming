#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while(T--)
    {
        int Na, Nb, Nc;
        cin >> Na >> Nb >> Nc;

        if (Na > (Nb + Nc))
        {
            cout << "YES" << endl;
        }
        else if (Nb > (Na + Nc))
        {
            cout << "YES" << endl;
        }
        else if (Nc > (Na + Nb))
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }

    return 0;
}