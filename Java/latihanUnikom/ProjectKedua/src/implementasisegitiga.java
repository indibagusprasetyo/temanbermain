import java.util.Scanner;

public class implementasisegitiga {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        System.out.println("Input panjang segitiga : ");
        int x = input.nextInt();
        for (int a = 1; a <= x; a++) {
            for (int b = 1; b <= a; b++) {
                if (b == 1 || a == x || a == b) System.out.print("* ");
                else System.out.print("   "); //space 3x times
            }
            System.out.println(" ");
        }
    }
}
