/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Equinox
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0)
        {
            int N = sc.nextInt();
            int A = sc.nextInt();
            int B = sc.nextInt();
            int c1 = 0, c2 = 0;
            String S;
            for (int i = 0; i < N; i++)
            {
                S = sc.next();
                if(S.charAt(0) == 'E' || S.charAt(0) == 'Q' || S.charAt(0) == 'U'|| S.charAt(0) == 'I'|| S.charAt(0) == 'N'|| S.charAt(0) == 'O'|| S.charAt(0) == 'X')
                    c1 += A;
                else
                    c2 += B;
            }
            
            if (c1 > c2)
                System.out.println("SARTHAK" );
            else if (c1 < c2)
                System.out.println("ANURADHA" );
            else
                System.out.println("DRAW" );
            


        }
	}
}
