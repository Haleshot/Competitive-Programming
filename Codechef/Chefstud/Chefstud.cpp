#include <iostream>
using namespace std;


int main()
{

    int T;
    cin >> T;
    while (T--)
    {
        string s;
        cin >> s;
        int c;
        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] == '<' && s[i + 1] == '<')
            {
                c++;
            }

        }
        cout << c << endl;

    }

    return 0;
}

