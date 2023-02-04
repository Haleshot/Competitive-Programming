#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    double A, B;
    char C;
    cin >> A >> B;
    cin >> C;
    
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
        cout << fixed << setprecision(1) <<  A * B << endl;
    }
    else if (C == '/')
    {
        cout << fixed << setprecision(8) << A / B << endl;
    }
    return 0;
}