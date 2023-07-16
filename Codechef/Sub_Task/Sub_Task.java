/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Sub_Task
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T > 0)
        {
            T -= 1;
            int one_count = 0;
            int N = sc.nextInt();
            int M = sc.nextInt();
            int K = sc.nextInt();
            ArrayList <Integer> A = new ArrayList<>();

            for (int i = 0; i < N; i++)
            {
                A.add(sc.nextInt());
            }
            for (int i = 0; i < N; i++)
            {
                if (A.get(i) == 1)
                {
                    one_count += 1;
                }
                else
                {
                    break;
                }
            }
            if (one_count == N)
                System.out.println(100);
            else if (one_count >= M)
                System.out.println(K);
            else
                System.out.println(0);

	    }
    }
}
