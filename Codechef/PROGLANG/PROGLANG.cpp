#include <iostream>
using namespace std;
#define MAX 2


int main()
{
    int T;
    cin >> T;
    while(T--)
    {
        int A, B, A1, B1, A2, B2, l1[MAX], l2[MAX];
        cin >> A >> B >> A1 >> B1 >> A2 >> B2;

        l1[0] = A1;
        l1[1] = B1;

        l2[0] = A2;
        l2[1] = B2;

        for (int i = 0; i < 2; i++)
        {
            if(A == l1[i] && B == l1[i])
            {
                cout << 1 << endl;
            }
            else if (A == l2[i] && B == l2[i])
            {
                cout << 2 << endl;
            }

            else
            {
                cout << 0 << endl;
            }
        }




    }
    return 0;
}