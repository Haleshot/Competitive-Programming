#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, X, Y, A, B, petrol, diesel;
        cin >> N >> X >> Y >> A >> B;
        petrol = (N/A)* X;
        diesel = (N/B)* Y;
        if (petrol > diesel)
        {
            cout << "DIESEL" << endl;
        }
        else if (petrol < diesel)
        {
            cout << "PETROL" << endl;
        }
        else
        {
            cout << "ANY" << endl;
        }
    }
    return 0;
}