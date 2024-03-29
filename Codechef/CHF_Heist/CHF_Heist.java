/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class CHF_Heist
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while (T-- > 0)
		{
			long D, d, P, Q;
			D = sc.nextLong();
			d = sc.nextLong();
			P = sc.nextLong();
			Q = sc.nextLong();
			long res = ((d * (D / d) * (2 * P + ((D / d) - 1) * Q)) / 2) + ((D % d) * (P + (D / d) * Q));
			System.out.println(res);
		}
		sc.close();
	}
}
