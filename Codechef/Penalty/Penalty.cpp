#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int A[10];
        for (int i = 0; i < 10; i++)
        {
            cin >> A[i];
        }
        if ((A[1] + A[3] + A[5] + A[7] + A[9]) > (A[2] + A[4] + A[6] + A[8] + A[10]))
        {
            cout << 1 << endl;
        }
        if ((A[1] + A[3] + A[5] + A[7] + A[9]) < (A[2] + A[4] + A[6] + A[8] + A[10]))
        {
            cout << 2 << endl;
        }
        else
        {
            cout << 0 << endl;
        }


    }
    return 0;
}