#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        int L[N];
        for (int i = 0; i < N; i++)
        {
            cin >> L[i];
        }
        int minimum = L[0], maximum = 0;
        for (int i = 0; i < N; i++)
        {
            if (L[i] < minimum)
                minimum = L[i];
            else if (L[i] - minimum > maximum)
                maximum = L[i] - minimum;
        }
        if (maximum > 0)
            cout << maximum << endl;
        else
            cout << "UNFIT" << endl;
    }
    return 0;
}