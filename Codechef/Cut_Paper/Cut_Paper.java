import java.util.Scanner;


public class Cut_Paper
{
    public static void main(String[] args) 
    {
        int T;
        Scanner sc = new Scanner(System.in);
        T = sc.nextInt();
        while(T > 0)
        {
            int N, K;
            N = sc.nextInt();
            K = sc.nextInt();
            System.out.println((N/K) * (N/K));
        }

        sc.close()

    }

}
