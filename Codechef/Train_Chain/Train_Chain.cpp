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
        string S[N];
        int A = 0, B = 0, AB = 0, O = 0;
        for (int i = 0;  i < N; i ++)
        {
            cin >> S[i];
            if (S[i] == "A")
            {
                A += 1;
            }
            else if (S[i] == "B")
            {
                B += 1;
            }
            else if (S[i] == "AB")
            {
                AB += 1;
            }
            else if (S[i] == "O")
            {
                O += 1;
            }
        }
    }
    return 0;
}