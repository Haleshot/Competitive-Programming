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
            salary -= 0.5 * salary;
            for (int i = 0; i < N - 1; i++)
            {
                salary -= 0.5*salary;
            }
            cout << salary << endl;
        }
    }

    return 0;
}