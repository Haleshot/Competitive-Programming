/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0){
		    int n = sc.nextInt();
		    int arr[] = new int[n];
		    for(int i=0;i<n;i++){
		        arr[i] = sc.nextInt();
		    }
		    int next[] = new int[n];
		    Stack<Integer> s = new Stack<>();
		    for(int i=n-1;i>=0;i--){
		        if(s.isEmpty()){
		            next[i] = -1;
		            s.push(arr[i]);
		        } else if(arr[i]>s.peek()){
		            next[i] = s.peek();
		            s.push(arr[i]);
		        } else{
		            while(!s.isEmpty() && arr[i]<=s.peek()){
		                s.pop();
		            }
		            if(s.isEmpty()){
		                next[i] = -1;
		            } else
		            next[i] = s.peek();
		            s.push(arr[i]);
		        }
		    }
		    for(int i=0;i<n;i++){
		        System.out.print(next[i]+" ");
		    }
		    System.out.println();
		}
	}
}