/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Slab
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0)
        {
            double N = sc.nextDouble();
            double net_total = 0;
            if (N <= 250000)
                net_total = N;

            else if (N > 250000 && N <= 500000)
                net_total = N - ((N - 250000) * 0.05); 
            
            else if (N > 500000 && N <= 750000)
                net_total = N - ((250000 * 0.05) + (N - 500000) * 0.1) ;
            
            else if (N > 750000 && N <= 1000000)
                net_total = N - ((250000 * 0.05) + (250000 * 0.1) + (N - 750000) * 0.15);
                
            else if (N > 1000000 && N <= 1250000)
                net_total = N - ((250000 * 0.05) + (250000 * 0.1) + (250000 * 0.15) + (N - 1000000) * 0.2);       

            else if (N > 1250000 && N <= 1500000)
                net_total = N - ((250000 * 0.05) + (250000 * 0.1) + (250000 * 0.15) + (250000 * 0.2) + (N - 1250000) * 0.25);       
            
            else if (N > 1500000)
                net_total = N - ((250000 * 0.05) + (250000 * 0.1) + (250000 * 0.15) + (250000 * 0.2) + (250000 * 0.25) + (N - 1500000) * 0.3);      
            
            System.out.println((int)(net_total));
        }
        sc.close();
	}
}
