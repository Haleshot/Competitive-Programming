#include <iostream>
using namespace std;

int main();
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        if (N <= 10)
            cout << "LOWER DOUBLE" << endl;
        else if (N >= 11 && N <= 15)
            cout << "LOWER SINGLE" << endl;
        else if (N >= 16 && N <= 25)
            cout << "UPPER DOUBLE"<< endl;
        else
            cout << "UPPER SINGLE"<< endl;
    }
    return 0;
}