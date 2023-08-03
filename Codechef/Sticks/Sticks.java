/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Sticks
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0)
        {
            int N = sc.nextInt();
            int[] A = new int[N];
		    for (int i  = 0; i < N; i++)
            {
		        A[i] = sc.nextInt();
		    }
		    Arrays.sort(A);
		    int l = 0, b = 0;
            for (int i  = N - 1; i >= 0; i--)
            {
                if(l == 0 && A[i] == A[i - 1])
                {
		            l = A[i];
		            i--;
		            continue;
		        }
		        else if(A[i] == A[i - 1])
                {
		            b = A[i];
		            break;
		        }
            }
            
        }
	}
}
