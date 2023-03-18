#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {   
        int X, Y, Z;
        cin >> X >> Y >> Z;
        if (X <= Y)
        {
            cout << Z << endl;
        }
        else
        {
            int i = 2;
            while (true)
            {
                int temp_Y, temp_Z;
                temp_Y = Y * i;
                temp_Z = Z * i;
                i += 1;
                if (X <= temp_Y)
                {
                    cout << temp_Z << endl;
                    break;
                }

            }
        }
    }
    return 0;
}