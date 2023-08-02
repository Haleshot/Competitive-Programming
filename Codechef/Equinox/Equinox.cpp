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
        string S;
        for (int i = 0; i < N; i++)
        {
            cin >> S;
            if(S[0] == 'E' || S[0] == 'Q' || S[0] == 'U'|| S[0] == 'I'|| S[0] == 'N'|| S[0] == 'O'|| S[0] == 'X')
                c1 += A;
            else
                c2 += B;
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