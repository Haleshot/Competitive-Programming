#include <iostream>
using namespace std;

int GCD(int a, int b)
{
    if(b == 0)
    return a;
    
    return GCD(b, a%b);
}

int main() 
{
    int T;
    cin >> T;
    while(T--)
    {
        int n;
        cin >> n;
        int arr[n];
        for(int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        int a = arr[0], b;
        for(int i = 1; i < n; i++)
        {
            b = arr[i];
            a = GCD(a,b);
        }
        for(int i = 0; i < n; i++)
        {
            arr[i] = arr[i]/a;
        }
        for(int i = 0; i < n; i++)
        {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    return 0;
}