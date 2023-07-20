/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Bath
{
	public static void main (String[] args) throws java.lang.Exception
	{
        Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
        while (T-- > 0)
        {
            int X = sc.nextInt();
            int y = sc.nextInt();
            System.out.println((X/(2 * Y)));
        }
	}
}
