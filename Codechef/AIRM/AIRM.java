/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class AIRM
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0)
        {
            int N = sc.nextInt();
            int A[] = new int[2 * N];
            for (int i = 0; i < 2 * N; i++)
                A[i] = sc.nextInt();

            Arrays.sort(A);
            int c = 1, maximum = 0;
            for (int i = 0; i < 2 * N - 1; i++)
            {
                if (A[i] == A[i + 1])
                    c += 1;
                else
                {
                    maximum = Math.max(maximum, c);
                    c = 1;
                }
            }
            maximum = Math.max(maximum, c);
            System.out.println(maximum);
        }
	}
}
