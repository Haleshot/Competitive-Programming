#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        int arr[N], dept[N];
        for (int i = 0; i < N; i++)
        {
            cin >> arr[i];
        }
        for (int i = 0; i < N; i++)
        {
            cin >> dept[i];
        }
        int current = 0, maximum = 0, i = 0, j = 0;
        while (i < N && j < N)
        {
            if (arr[i] < dept[j])
                {
                    i += 1;
                    current += 1;
                }
            if (current > maximum)
                maximum = current;
            else
                {
                    j += 1;
                    current -= 1;
                }
            
        }
    }
    return 0;
}