/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class How_Many
{
	public static void main (String[] args) throws java.lang.Exception
	{
        Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
        String number = Integer.toString(N);
        int size = number.length();

        if (size == 1)
            System.out.println("1");
        else if (size == 2)
            System.out.println("2");
        else if (size == 3)
            System.out.println("3");
        else
            System.out.println("More than 3 digits");

        
	}
}
