#include <iostream>
using namespace std;

int main()
{
    int Test;
    cin >> Test;
    while (Test--)
    {
        string S, T;
        cout << endl;
        cin >> S >> T;
        for (int i = 0; i < 5; i++)
        {
            if (S[i] == T[i])
            {
                cout << "G";
            }
            else
            {
                cout << "B";
            }
        }
    }
    return 0;
}