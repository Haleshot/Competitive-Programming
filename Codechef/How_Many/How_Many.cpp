#include <iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;
    int size = to_string(N).length();

    if (size == 1)
    cout << ("1");
    else if (size == 2)
        cout << ("2");
    else if (size == 3)
        cout << ("3");
    else
        cout << ("More than 3 digits");

    return 0;
}