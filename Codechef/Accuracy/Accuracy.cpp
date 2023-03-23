#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        float X;
        int temp;
        cin >> X;
        temp = ceil(X/3);
        temp *= 3;
        cout << temp - X << endl;

    }
    return 0;
}