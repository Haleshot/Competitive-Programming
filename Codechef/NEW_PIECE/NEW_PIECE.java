/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class NEW_PIECE
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0)
        {
            int A = sc.nextInt();
            int B = sc.nextInt();
            int P = sc.nextInt();
            int Q = sc.nextInt();
            if (((A == P) && (B == Q)))
                System.out.println(0);
            else if ((A + B) % 2 == (P + Q) % 2)
                System.out.println(2);
            else
                System.out.println(1);
        }
	}
}
