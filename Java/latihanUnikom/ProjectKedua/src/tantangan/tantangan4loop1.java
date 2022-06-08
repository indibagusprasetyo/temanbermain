package tantangan;
import java.util.Scanner;

public class tantangan4loop1 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        System.out.println("Dari : "); int dari = input.nextInt();

        System.out.println("Sampai : "); int sampai = input.nextInt();

        for (int i = dari; i <= sampai; i++) {
            if (i % 2 == 0) {
                System.out.println(i + " ");
            }
        }
    }
}