import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
    	int n1 = s.nextInt();
    	int n2 = s.nextInt();
    	int n3 = s.nextInt();
    	int num = 9*1 + 7*3 + 8*1 + 0*3 + 9*1 + 2*3 + 1*1 + 4*3 + 1*1 + 8*3;
    	num += n1*1 + n2*3 + n3*1;
    	System.out.println("The 1-3-sum is "+num);
    }
}