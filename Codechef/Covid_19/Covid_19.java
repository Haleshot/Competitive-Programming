/* package codechef; // don't place package name! */

import java.util.*;

import javax.print.DocFlavor.INPUT_STREAM;

import java.lang.*;
import java.lang.Math;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Covid_19
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        while (T-- > 0)
        {
            int N = sc.nextInt();
            int X[] = new int[N];
            int c = 1, min = 100, max = 1;
            for (int i = 0; i < N; i++)
            {
                X[i] = sc.nextInt();
            }
            for (int i = 0; i < N - 1; i++)
            {
                if (Math.abs(X[i + 1] - X[i]) <= 2)
                    c++;
                else
                {
                    if (c > max)
                        max = c;
                    if (c < min)
                        min = c;   
                        c = 1;
                    
                }
            }
            if (c > max)
                max = c;
            if (c < min)
                min = c;   
                c = 1;
            
            System.out.println(min + " " + max);

        }
	}
}
