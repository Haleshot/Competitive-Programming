/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0)
        {
            String J = sc.next();
            String S = sc.next();
            HashMap<Character, Integer> m = new HashMap<>();
            for (char ch:J.toCharArray())
                m.put(ch, m.getOrDefault(ch, 0) + 1);
            int count = 0;
            for (int i = 0; i < S.length(); i++)
            {
                char temp = S.charAt(i);
                if (m.containsKey(temp))
                    count += 1;
            }


        }
	}
}
