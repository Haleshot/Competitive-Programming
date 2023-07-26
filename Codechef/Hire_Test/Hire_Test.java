/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Hire_Test
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0)
        {
            int N = sc.nextInt();
            int M = sc.nextInt();
            int X = sc.nextInt();
            int Y = sc.nextInt();
            String[] inp = new String[N];
            for (int i = 0; i< N; i++)
            {
                inp[i] = sc.next();
            }
            for (int i = 0; i < N; i++)
            {
                int F_Count = 0, P_Count = 0;
                for (int j = 0; j < M; j++)
                {
                    if (inp[i].charAt(j) == 'P')
                    {
                        P_Count += 1;
                    }
                    else if ((inp[i].charAt(j) == 'F'))
                    {
                        F_Count += 1;
                    }
                }
                if (F_Count >= X || (F_Count >= (X - 1) && P_Count >= Y))
                {
                    System.out.println("1");
                }
                else
                {
                    System.out.println("0");
                }
            }

        }
	}
}
