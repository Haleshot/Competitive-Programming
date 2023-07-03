#include <iostream>
using namespace std;

int S(string S)
{
    int balance = 0, max_balance = 0;
    for (int i = 0; i < S.size(); i++)
    {
        for (int i = 0; i < S.size();i++)
        {
            if (S[i] == '(')
                balance += 1;
            if (S[i] == ')')
                balance -= 1;
            
            max_balance = max(max_balance, balance);
        }
    }
    return max_balance;
}


int main()
{
    int T;
    cin >> T;
    while (T--)
    {
       string A;
       cin >> A;
       int result = S(A);
       for (int i = 0; i < result; i++)
       {
            cout << "(";
       }
       for (int i = 0; i < result; i++)
       {
            cout << ")";
       }
    }
    return 0;
}