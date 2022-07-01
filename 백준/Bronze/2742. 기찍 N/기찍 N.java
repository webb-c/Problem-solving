import java.util.Scanner;

class Main { 								 //백준 : public 없애고 Test -> Main으로 변경
	public static void main(String args[]) {
		Scanner s = new Scanner(System.in);
		int num = s.nextInt();
		
		for(int i=num ; i>=1 ; i--)
			System.out.println(i);
	}
}
