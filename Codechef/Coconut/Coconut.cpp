#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int xa, xb, Xa, Xb, req_1, req_2;
        cin >> xa >> xb >> Xa >> Xb;
        req_1 = Xa/xa;
        req_2 = Xb/xb;
        cout << req_1 + req_2 << endl;
    }   
    return 0;
}