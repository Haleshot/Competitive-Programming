#include <iostream>
using namespace std;

int main()
{
    int N, K, ele, c = 0;
    cin >> N >> K;
    for (int i = 0; i < N; i++)
    {
        cin >> ele;
        if (ele % K == 0)
        {
            c += 1;
        }
    }
    cout << c << endl;
    return 0;
}