#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
            int W, X, Y, Z, c, total;
            cin >> W >> X >> Y >> Z;
            c = Y * Z;
            total = W + c;
            if (total > X)
            {
                cout << "Overflow" << endl;
            } 
            if (total < X)
            {                
                cout << "Unfilled" << endl;
            }
            if (total == X)
            {
                cout << "Filled" << endl;
            }
    }
    return 0;
}