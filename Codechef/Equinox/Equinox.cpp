#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, A, B, c1 = 0, c2 = 0;
        cin >> N >> A >> B;
        string S[N];
        for (int i = 0; i < N; i++)
        {
            cin >> S[i];
            if (S[i] == "E" || S[i] == "Q" || S[i] == "U" ||  S[i] == "I" || S[i] == "N" || S[i] == "O" || S[i] == "X" )
                c1 += 1;
            else
                c2 += 1;
        }
        if (c1 > c2)
            cout << "SARTHAK" << endl;
        else if (c1 < c2)
            cout << "ANURADHA" << endl;
        else
            cout << "DRAW" << endl;

    }
    return 0;
}