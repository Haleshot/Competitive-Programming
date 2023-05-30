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
        
    }
    return 0;
}