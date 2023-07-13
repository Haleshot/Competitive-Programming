import java.util.Scanner;

public class Rating
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        while (T > 0)
        {
            T -= 1;
            int S = sc.nextInt();
            System.out.println(-S - 1);

        }

        sc.close();
    }
}