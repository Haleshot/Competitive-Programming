#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, remain, c = 0;
        float atten_perc = 0;
        string B;
        cin >> N;
        cin >> B; 
        for (int i = 0; i < B.length(); i++)
        {
            if (B[i] == '1')
            {
                c += 1;
            }
        }
        remain = 120 - N + c;
        atten_perc = (remain/120) * 100;
        cout << atten_perc << endl;
        if (atten_perc >= 75.0)
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