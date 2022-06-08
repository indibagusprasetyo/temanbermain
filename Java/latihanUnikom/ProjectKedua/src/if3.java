public class if3 {
    public static void main(String args[]) {
        if (true) {
            //Aksi true
        } else if (true) {
            //Aksi true kedua
        } else {
            //Aksi false
        }

        //contoh
        int nilai = 100;

        if (nilai > 80) {
            System.out.println("Indeks : A");
        } else if (nilai > 70) {
            System.out.println("Indeks : B");
        } else {
            System.out.println("Indeks : C");
        }
    }
}
