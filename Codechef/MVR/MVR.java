/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class MVR
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int X = sc.nextInt();
        int Y = sc.nextInt();

        if (((2 * A) + B) > ((2 * X) + Y))
        {
           System.out.println("MESSI");
        }
        else if (((2 * A) + B) < ((2 * X) + Y))
        {
           System.out.println("RONALDO");
        }
        else
        {
           System.out.println("EQUAL");
        }
	}
}
