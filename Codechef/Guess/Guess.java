/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Guess
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0)
        {
            int N = sc.nextInt();
            int M = sc.nextInt();
            long total = N * M;
            if (N == 1 && M == 1)
                System.out.println("0/1");

            else if (N % 2 == 0 || M % 2 == 0)
            {
                System.out.println("1/2" );
            }

            else
            {
                long temp = total / 2;
                System.out.println(temp + "/" + total);
            }
                
            }
        sc.close();
	}
}
