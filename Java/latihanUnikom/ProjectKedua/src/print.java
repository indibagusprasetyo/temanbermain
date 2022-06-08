public class print {
    public static void main(String args []) {
        String nama = "Indi";
        short usia = 20;
        char goldar = 'O';
        float tinggiBadan = 171.922f;
        boolean jomblo = false;

        System.out.printf("Halo, nama saya " + nama + "\n");
        System.out.printf("Usia saya" + usia + "tahun\n");
        System.out.printf("Golongan darah " + goldar + "\n");
        System.out.printf("Tinggi badan " + tinggiBadan + "\n");
        System.out.printf("Saya " + (jomblo ? "sudah menikah" : "masih aja jomblo"));
    }
}
