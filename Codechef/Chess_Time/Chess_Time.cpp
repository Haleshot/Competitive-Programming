#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while(T--)
    {
        int N;
        cin >> N;
        N *= 60;
        cout << N/20 << endl;
    }

    return 0;

}