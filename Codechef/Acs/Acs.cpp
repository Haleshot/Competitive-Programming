#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int P, R;
        cin >> P;
        R = (P % 100) + (P / 100);
        if (R <= 10)
        {
            cout << R << endl;
        }
        else
        {
            cout << -1  << endl;
        }
    }
    return 0;
}