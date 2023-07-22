/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.util.Arrays;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Walk
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0)
        {
            int N = sc.nextInt();
            int[] W = new int[N];
            for (int i = 0; i < N; i++)
            {
                W[i] = sc.nextInt();
            }
            for (int i = 0; i < N; i++)
            {
                W[i] += i;
            }
            System.out.println(Arrays.stream(W).max().getAsInt());
        }
	}
}
