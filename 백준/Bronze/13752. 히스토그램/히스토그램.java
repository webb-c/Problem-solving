import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
    	int count = s.nextInt();
    	for(int i = 0 ; i<count ; i++) {
    		int num = s.nextInt();
    		for(int j = 0 ; j < num ; j++) {
    			System.out.print("=");
    		}
    		System.out.println();
    	}
    }
}