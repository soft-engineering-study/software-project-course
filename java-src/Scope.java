package java;
public class Scope {
    // field that is accessible to all methods of this class
    private static int x = 1;

    // method main creates and initializes local variable x
    // and calls methods useLocalVariable and useField
    public static void main(String[] args) {
        int x =5; // method's local variable x shadows field x

        System.out.printf("local x in main is %d%n", x);

        useLocalVariable(); //  useLocalVariable has local x
        useField(); // useField uses class Scope's field x
        useLocalVariable(); // useLocalVariable reinitilizes local x
        useField(); // class Scope's field x returns its value

        System.out.printf("%nlocal x in main is %d%n", x);
    }

    // create and initialize local variable x during each call
    public static void useLocalVariable(){
        int x = 25;

        System.out.printf("%nlocal x in main is %d%n", x);
    }

    // modify class Scope's fields x during each call
    public static void useField() {
        System.out.printf("%nfield x on entering method useField is %d%n", x);
        x *= 10; // modifies class Scope's field x
        System.out.printf("field x before exiting method useField is %d%n", x);
    }

}
