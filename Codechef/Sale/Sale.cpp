#include <iostream>
#include <algorithm>
using namespace std;

bool compare(int a, int b)
{
    return(a < b);
}

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int A, B, C, minimum;
        cin >> A >> B >> C;
        minimum = min({A, B, C}, compare);
        cout << ((A + B + C) - minimum) << endl;

    }
    return 0;
}