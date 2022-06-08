package tantangan;
import java.util.Scanner;


public class tantangan4loop2 {
    public static void main(String arrgs[]) {
        int tangga = 0;
        Scanner input = new Scanner(System.in);
        System.out.print("Jumlah Anak Tangga = "); tangga = input.nextInt();

        if (tangga > 0) {
            for (int i = 1; i <= tangga; i++) {
                for (int j = tangga - 1; j >= i; j--) {
                    System.out.print(" ");
                }
                for (int k = 1; k <= i; k++) {
                    System.out.print("4");
                }
                System.out.println();
            }
        } else {
            System.out.print("Masukan Bilangan Positif > 0");
        }
    }
}
