#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, remain;
        float atten_perc;
        string B;
        cin >> N;
        cin >> B;
        remain = 120 - N;
        atten_perc = (remain/120) * 100;
        if (atten_perc >= 75)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }

    }



    return 0;
}