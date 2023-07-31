/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Seat_Number
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0)
        {
            int N = sc.nextInt();
            if (N <= 10)
                System.out.println(("LOWER DOUBLE"));
            else if (N >= 11 && N <= 15)
                System.out.println(("LOWER SINGLE"));
            else if (N >= 16 && N <= 25)
                System.out.println(("UPPER DOUBLE"));
            else
                System.out.println(("UPPER SINGLE"));
        }
	}
}
