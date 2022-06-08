import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bufferedreader {
    public static void main(String args []) {
        try {
            BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

            System.out.print("Masukan Nama Anda :");
            String nama = input.readLine();

            System.out.print("Masukan Tinggi Badan Anda :");
            float tinggiBadan = Float.parseFloat(input.readLine());

            System.out.printf("Nama Anda %s\n", nama);
            System.out.printf("Tinggi Badan Anda %.2f", tinggiBadan);
            } catch (IOException e) {
                System.out.println("Mohon Masukan Input Dengan Benar");
            }
        }
    }
