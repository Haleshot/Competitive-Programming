/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
public class Best_Of_Two 
{
    public static void main(String args[]) 
    {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while( T-- > 0 ) 
        {
            int X = sc.nextInt();
            int Y = sc.nextInt();
            System.out.println( Math.max(X, Y) );
        }
    }
}