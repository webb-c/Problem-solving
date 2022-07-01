import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
    	int count = s.nextInt();
    	int num1, num2;
    	for(int i = 0; i<count; i++) {
    		num1 = s.nextInt();
    		num2 = s.nextInt();
    		System.out.println(num1+num2);
    	}

    }
}