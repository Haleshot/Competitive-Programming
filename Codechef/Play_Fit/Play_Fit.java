/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Play_Fit
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0)
        {
            int N = sc.nextInt();
            int[] L = new int[N];
            for (int i = 0; i < N; i++)
            {
                L[i] = sc.nextInt();
            }
            int minimum = L[0], maximum = 0;
            for (int i = 0; i < N; i++)
            {
                if (L[i] < minimum)
                    minimum = L[i];
                else if (L[i] - minimum > maximum)
                    maximum = L[i] - minimum;
            }
            if (maximum > 0)
                System.out.println(maximum);
            else
                System.out.println("UNFIT");

        }
	}
}
