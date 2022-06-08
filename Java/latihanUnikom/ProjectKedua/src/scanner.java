import java.util.Scanner;

public class scanner {
    public static void main(String args[]) {
        try (Scanner input = new Scanner(System.in)) {
            System.out.print("Masukan Nama Anda : ");
            String nama = input.nextLine();

            System.out.print("Masukan Tinggi Badan Anda : ");
            float tinggiBadan = input.nextFloat();

            System.out.printf("Nama Anda %s\n", nama);
            System.out.printf("Tinggi Badan Anda %.2f", tinggiBadan);
        }

    }
}
