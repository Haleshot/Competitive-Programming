/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Horses
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while(T > 0){
		    int N = sc.nextInt();    
		    int S[] = new int[N]; 
		    for (int i = 0 ; i < N ; i++ ) 
                S[i] = sc.nextInt();
		    Arrays.sort(S);
		    int min = Integer.MAX_VALUE;
		    for ( int i = 0  ; i < N - 1 ; i++ ) {
		        min = Math.min( min , S[i + 1] - S[i] );
		    }
		    System.out.println( min );
		    
		}
	}
}