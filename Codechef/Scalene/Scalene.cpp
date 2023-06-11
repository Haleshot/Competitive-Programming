#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int A, B, C, scalene[3];
        vector<int> arr;
        cin >> A >> B >> C;
        arr.push_back(A);
        arr.push_back(B);
        arr.push_back(C);
        cout << arr << endl;
    }
    return 0;
}
 