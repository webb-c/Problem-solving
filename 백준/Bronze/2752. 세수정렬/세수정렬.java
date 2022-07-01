import java.util.Scanner;

class Main { 								 //백준 : public 없애고 Test -> Main으로 변경
	public static void main(String args[]) {
		Scanner s = new Scanner(System.in);
		int num1 = s.nextInt();
		int num2 = s.nextInt();
		int num3 = s.nextInt();
		
		int tum;
		
		if(num1 > num2) {
			tum = num1;
			num1 = num2;
			num2 = tum;
			if(num1 > num3) {
				tum = num1;
				num1 = num3;
				num3 = tum;
			}
		}
		else {
			if(num1 > num3) {
				tum = num1;
				num1 = num3;
				num3 = tum;
			}
		}
		
		if(num2 > num3) {
			tum = num2;
			num2 = num3;
			num3 = tum;
		}
		
		System.out.print(num1+" ");
		System.out.print(num2+" ");
		System.out.print(num3);		
	}
}
