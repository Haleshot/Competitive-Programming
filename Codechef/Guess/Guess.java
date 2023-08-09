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
            if ((N * M) % 2 == 0)
                System.out.println("1/2");
            
            else
                System.out.println(Math.floor((N * M) / 2) + "/" + (N * M));
            
        }
        sc.close();
	}
}
