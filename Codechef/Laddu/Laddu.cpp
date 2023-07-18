#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N, A;
        string ori;
        cin >> N >> ori;
        int points = 0;
        string all_inputs;
        for (int i = 0; i < N; i++)
        {
            cin >> all_inputs;
            if(all_inputs == "CONTEST_WON" || all_inputs == "BUG_FOUND")
            cin >> A;
            if(all_inputs == "CONTEST_WON") 
            {
                points += 300; 
                if(A <= 20)
                    points += 20 - A;
            }
            if(all_inputs == "BUG_FOUND") 
                points += A;
            if(all_inputs == "TOP_CONTRIBUTOR")
                points += 300;
            if(all_inputs == "CONTEST_HOSTED")
                points += 50;

        }
        if(ori == "INDIAN")
            cout << points/200 << endl;
        else
            cout << points/400 << endl;
    }
    return 0;
}