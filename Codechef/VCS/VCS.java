/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.util.Scanner;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class VCS
{
	public static void main (String[] args) throws java.lang.Exception
	{
        Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
        while (T > 0)
        {
            T -= 1;
            int first = 0, second = 0;
            int N = sc.nextInt();
            int M = sc.nextInt();
            int K = sc.nextInt();
            ArrayList <Integer> A = new ArrayList<>();
            ArrayList <Integer> B = new ArrayList<>();

            for (int i = 0; i < M; i++)
            {
                A.add(sc.nextInt());
            }

            for (int i = 0; i < K; i++)
            {
                B.add(sc.nextInt());
            }

            for (int i = 1; i < N + 1; i++)
            {
                if (A.contains((i)) && B.contains(i))
                {
                    first += 1;
                }
                else if (!A.contains((i)) && !B.contains(i))
                {
                    second += 1;
                }
            }

            System.out.println(first + " " + second);

        }
        sc.close();

	}
}
