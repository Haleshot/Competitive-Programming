#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int X, Y, Z;
        if (X > Y)
        {
            if (X > Z)
            {
                cout << "Setter" << endl;
            }
            else
            {
                cout << "Editorialist" << endl;
            }
        }
        else
        {
            if (Y > Z)
            {
                cout << "Tester" << endl;
            }
            else
            {
                cout << "Editorialist" << endl;
            }
        }
    }
    return 0;
}