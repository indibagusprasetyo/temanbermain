public class printf {
    public static void main(String args []) {
        String nama = "Indi";
        short usia = 20;
        char goldar = 'O';
        float tinggiBadan = 171.922f;
        boolean jomblo = true;

        System.out.printf("Halo, nama saya %s\n", nama);
        System.out.printf("Usia saya %d tahun\n", usia);
        System.out.printf("Golongan darah %c\n", goldar);
        System.out.printf("Tinggi badan %.2f\n", tinggiBadan);
        System.out.printf("Anda Jomblo? %b\n", jomblo);
    }
}