package tantangan;
import java.util.Scanner;

class Segitiga {
    int alas,tinggi;

    //constructor
    Segitiga(int inputAlas,int inputTinggi) {
        this.alas = inputAlas;
        this.tinggi = inputTinggi;
    }

    public void show() {
        System.out.println("Alas   : " + this.alas);
        System.out.println("Tinggi : " + this.tinggi);
    }

    public void setAlas(int alas) {
       this.alas = alas;
    }

    public void setTinggi(int tinggi) {
        this.tinggi = tinggi;
    }

    public void getluas() {
        System.out.println("Luas Segitiga : " + (this.alas*this.tinggi)/2);
    }  
}

public class segitiga1 {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);

        System.out.println("========= Set Alas * Tinggi =========");
        System.out.print("Masukan Alas Segitiga : ");
        int alas = input.nextInt();

        System.out.print("Masukan Tinggi Segitiga : ");
        int tinggi = input.nextInt();
        
        Segitiga segitiga1 = new Segitiga(alas, tinggi);
        segitiga1.show();
        segitiga1.getluas();

        System.out.println("========= Update Alas & Tinggi =========");
        System.out.print("Masukan Alas Segitiga : ");
        alas = input.nextInt();

        System.out.print("Masukan Tinggi Segitiga : ");
        tinggi = input.nextInt();

        segitiga1.setAlas(alas); //Memperbarui alas var segitiga1
        segitiga1.setTinggi(tinggi); //Memperbarui tinggi var segitiga1
        segitiga1.show(); //Menampilkan Alas & Tinggi Segitiga
        segitiga1.getluas(); //Menentukan Luas Segitiga

    }
}