/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Laddu
{
	public static void main (String[] args) throws java.lang.Exception
	{
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0)
        {
            int activities, points = 0;
            activities = sc.nextInt();
            String origin = sc.next();

            for (int i = 0; i < activities; i++)
            {
                String all_inputs = sc.next();
                if (all_inputs.equals("CONTEST_WON"))
                {
                    int rank = sc.nextInt();
                    if (rank <= 20)
                    {
                        points += 300 + (20 - rank);
                    }
                    else
                        points += 300; 
                }
                else if (all_inputs.equals("BUG_FOUND"))
                {
                    int severity = sc.nextInt();
                    points += severity; 
                }
                else if (all_inputs.equals("TOP_CONTRIBUTOR"))
                {
                    points += 300; 
                }
                else
                    points += 50;
            }
            if (origin.equals("INDIAN"))
                System.out.println(points/200);
            else
                System.out.println(points/400);

        }
	}
}
