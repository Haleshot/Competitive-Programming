#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    
    while (T--)
    {
        int X, Y, expense;
        cin >> X >> Y;
        expense = 30 * Y;
        if (expense <= X)
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