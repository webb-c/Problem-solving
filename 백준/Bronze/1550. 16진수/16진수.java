import java.util.Scanner;

class Main {
	public static void main(String args[]) {
		Scanner s = new Scanner(System.in);
		String num = s.nextLine();
		System.out.println(Integer.parseInt(num, 16));
	}
}
