import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	int num1=0;
    	int num2=0;
        Scanner s = new Scanner(System.in);
        num1=s.nextInt();
        num2=s.nextInt();
        System.out.print(num2 + (num2-num1));
    }
}
