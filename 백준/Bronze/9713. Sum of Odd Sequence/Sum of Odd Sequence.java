import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
    	int count = s.nextInt();
    	int sum = 0;
    	int num = 0;
    	for(int i = 0 ; i < count ; i++) {
    		sum = 0;
    		num = s.nextInt();
    		for(int j = 1; j<=num ; j+=2) {
    			sum += j;
    		}
    		System.out.println(sum);
    	}
    }
}