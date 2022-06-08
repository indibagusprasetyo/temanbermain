public class switch1 {
    public static void main(String args[]) {
        int bulan = 2;
        switch(bulan) {
            case 1:
                System.out.println("Bulan Januari");
                break;
            case 2:
                System.out.println("Bulan Februari");
                break;
            case 3:
                System.out.println("Bulan Maret");
                break;
            default:
                System.out.println("Angka bulan tidak valid");
        }
    }
}
