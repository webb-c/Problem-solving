import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	int s = sc.nextInt();
    	int a = sc.nextInt();
    	int t;
    	
    	if(a > s) {
    		t = s;
    		s = a;
    		a = t;
    	}
    	
    	System.out.println(a/2);
    }
}