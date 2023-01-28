#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        int X, N, score;
        cin >> X >> N;
        X /= 10;
        score = X * N;
        cout << score << endl;

    }
    
    return 0;

}