package java;
import java.util.ArrayList;

public class ArrayListCollection {
    public static void main(String[] args) {
        ArrayList<String> items = new ArrayList<String>();

        items.add("red");
        items.add(0, "yellow");

        System.out.print("Display list of contents with counter-controlled loop");

        for(int i = 0; i < items.size(); i++) {
            System.out.printf(" %s", items.get(i));
        }

        display(items, "%nDisplay list contents with enhanced for statement: ");

        items.add("green");
        items.add("yellow");
        display(items, "List with two new elemeents: ");

        items.remove("yellow");
        display(items, "Remove the first instance of yellow: ");

        items.remove(1);
        display(items, "Remove the second list element (green): ");

        System.out.printf("\"red\" is %sin the list %n", items.contains("red") ? "" : "not ");

        // display number of elements in the list
        System.out.printf("Size: %s%n", items.size());
    }

    public static void display(ArrayList<String> items, String header) {
        System.out.printf(header);

        for(String item : items)
            System.out.printf(" %s", item);
    }
}
