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
        int net_total = 0;
        
        if (N <= 250000)
            net_total = N;

        else if (N > 250000 and N <= 500000)
            net_total = N - ((N - 250000) * 0.05); 
        
        else if (N > 500000 and N <= 750000)
            net_total = N - ((250000 * 0.05) + (N - 500000) * 0.1) ;
        
        else if (N > 750000 and N <= 1000000)
            net_total = N - ((250000 * 0.05) + (250000 * 0.1) + (N - 750000) * 0.15);
            
        else if (N > 1000000 and N <= 1250000)
            net_total = N - ((250000 * 0.05) + (250000 * 0.1) + (250000 * 0.15) + (N - 1000000) * 0.2);       

        else if (N > 1250000 and N <= 1500000)
            net_total = N - ((250000 * 0.05) + (250000 * 0.1) + (250000 * 0.15) + (250000 * 0.2) + (N - 1250000) * 0.25);       
        
        else if (N > 1500000)
            net_total = N - ((250000 * 0.05) + (250000 * 0.1) + (250000 * 0.15) + (250000 * 0.2) + (250000 * 0.25) + (N - 1500000) * 0.3);      
        
        cout << int(net_total) << endl;


     }
    return 0;
}