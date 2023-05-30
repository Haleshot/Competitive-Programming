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
        int odd[5], even[5];
        for (int i = 0; i < 10; i++)
        {
            if (i % 2 == 1)
            {
                odd[i] = A[i];
            }
            else if (i % 2 == 0)
            {
                even[i] = A[i];
            }
        }
        int odd_one_count[5], even_one_count[5];
        for (int i = 0; i < 5; i++)
        {
            if (odd[i] == 1)
            {
                odd_one_count[i] = A[i];
            }
        }
        for (int i = 0; i < 5; i++)
        {
            if (even[i] == 1)
            {
                even_one_count[i] = A[i];
            }
        }


        if (odd_one_count > even_one_count)
        {
            cout << 2 << endl;;
        }
        else if (odd_one_count < even_one_count)
        {
            cout << 1 << endl;;
        }
        else
        {
            cout << 0 << endl;
        }



    }
    return 0;
}