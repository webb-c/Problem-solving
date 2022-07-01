import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
    	int sum=0;
    	int num = s.nextInt();
    	for(int i = 1; i<=num ; i++) {
    		sum += i;
    	}
    	System.out.println(sum);
    }
}