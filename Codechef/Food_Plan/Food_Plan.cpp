#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        float N, M, least;
        cin >> N >> M;
        N -= 0.1*N;
        least = min(N, M);

        if (M == N)
        {
            cout << "EITHER" << endl;
        }
        else if (least == N)
        {
            cout << "ONLINE" << endl;
        }
        else if (least == M)
        {
            cout << "DINING" << endl;
        }

    }
    return 0;
}