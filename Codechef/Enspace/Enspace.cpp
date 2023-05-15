#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while(T--)
    {
        int N, X, Y, tot;
        cin >> N >> X >> Y;
        tot = X + (2 * Y);
        if (tot > N)
        {
            cout << "NO" << endl;
        }
        else
        {
            cout << "YES" << endl;
        }
        
    }
    return 0;
}