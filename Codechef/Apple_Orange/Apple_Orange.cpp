#include <iostream>
using namespace std;


int HCF(int a, int b)
{
    if(b == 0)
    {
        return abs(a);
    }
    else return HCF(b, a % b);

}

int main()
{

    int T;
    cin >> T;

    while(T--)
    {
        int N, M;
        cin >> N >> M;
        int result = HCF(N, M);
        cout << result << endl;
    }
    return 0;
}