#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, U, D;
        cin >> N >> U >> D;
        int H[N], l1, l2, c = 1, c1 = 0;
        for (int i = 0; i < N; i++)
        {
            cin >> H[i];
        }
        for (int i = 0; i < N; i++)
        {
            l1 = H[i];
            l2 = H[i + 1];
            if (((l2 - l1) <= U) and ((l2 - l1) > 0))
                c += 1;

            else if ((l1 - l2) > D and c1 == 0)
            {
                c1 += 1;
                c += 1;
            }
        
            else if ((((l1 - l2) <= D) and c1 <= 1) and ((l1 - l2) > 0))
                c += 1;

            else if ((l1 - l2) == 0)
                c += 1;
            else
                break;
        }
        cout << c << endl;

    }
    return 0;
}