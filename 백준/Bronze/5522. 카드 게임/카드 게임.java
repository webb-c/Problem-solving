import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	int sum=0;
        Scanner s = new Scanner(System.in);
        for(int i = 0 ; i<5 ; i++) sum+=s.nextInt();
        System.out.print(sum);
    }
}