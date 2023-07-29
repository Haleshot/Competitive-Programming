import java.util.*;

public class Best_Of_Two {
    public static void main(String args[]) {
        Scanner scn = new Scanner(System.in);
        int T = scn.nextInt();
        while( T-- > 0 ) {
            int x = scn.nextInt();
            int y = scn.nextInt();
            System.out.println( Math.max( x, y) );
        }
    }
}