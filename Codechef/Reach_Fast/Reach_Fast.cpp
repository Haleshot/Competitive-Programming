#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        float X, Y, K;
        float least;
        cin >> X >> Y >> K;
        if (X <= Y)
        {
            least = ceil((Y - X)/K);
        }
        else if (X >= Y)
        {
            least = ceil((X - Y)/K);
        }
        else
        {
            cout << 0 << endl;
        }
        cout << least << endl;

    }
    return 0;
}