import java.util.Scanner;

class Main { 							
	public static void main(String args[]) {
		Scanner s = new Scanner(System.in);
		int num1, num2;
		int count = s.nextInt();
		
		for(int i=0 ; i<count ; i++) {
			num1 = s.nextInt();
			num2 = s.nextInt();
			if(num1>=num2) System.out.println("MMM BRAINS");
			else System.out.println("NO BRAINS");
		}
	}
}
