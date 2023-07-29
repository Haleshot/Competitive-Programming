import java.util.*;

public class Best_Of_Two 
{
    public static void main(String args[]) 
    {
        Scanner scn = new Scanner(System.in);
        int T = scn.nextInt();
        while( T-- > 0 ) 
        {
            int X = scn.nextInt();
            int Y = scn.nextInt();
            System.out.println( Math.max(X, Y) );
        }
    }
}