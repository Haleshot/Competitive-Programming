#include <iostream>
using namespace std;


int main()
{

    int A, B;
    char C;
    cin >> A >> B >> C;
    
    if (C == '+')
    {
        cout << A + B << endl;
    }
    else if (C == '-')
    {
        cout << A - B << endl;
    }
    else if (C == '*')
    {
        cout << A * B << endl;
    }
    else if (C == '/')
    {
        cout << A / B << endl;
    }


    return 0;
}