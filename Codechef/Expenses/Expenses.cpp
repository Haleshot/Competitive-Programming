#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, X, salary;
        cin >> N >> X;
        salary = pow(X, 2);
        if (N == 1)
        {
            cout << (salary - 0.5 * salary) << endl;
        }
        else
        {
            
        }
    }

    return 0;
}