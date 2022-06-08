public class continue1 {
    public static void main(String args[]) {
        for (int i = 0; i < 10; i++) {
            if (i == 3) {
                System.out.println("ENTER PIT STOP");
                continue;
            }
            System.out.printf("Lap ke %d\n", i);
        }
    }
}
