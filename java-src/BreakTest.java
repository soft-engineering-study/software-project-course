
public class BreakTest {
    public static void main(String[] args) {
        int count; // control variable also used after loop terminates

        for (count = 1; count <= 10; count++) { // loop 10 times
           if(count == 5) // terminates the loop if count = 5
               break;
           System.out.printf("%d ", count);
        }

        System.out.printf("%nBroke out of loop at count = %d%n", count);

    }
}
