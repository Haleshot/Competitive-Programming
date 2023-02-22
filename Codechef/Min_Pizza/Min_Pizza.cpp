#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, X;
        float slices;
        cin >> N >> X;
        slices = N * X;
        cout << ceil(slices/4) << endl;
    }
    return 
    0;
}