package java;
public class InitArray {

    public static void main(String[] args) {
//        //int[] array = new int[10];
//        int[] array = {32,27,64,18,95,14,90,70,60,37};
//
//        System.out.printf("%s%8s%n", "Index", "Value"); // column headings
//
//        // output each array element's value
//        for (int counter = 0; counter < array.length; counter++)
//            System.out.printf("%s%8s%n", counter, array[counter]);


        int[][] array1 = {{1,2,3},{4,5,6}};
        int[][] array2 = {{1,2}, {3}, {4,5,6}};

        System.out.println("Values in array1 by row are");
        outputArray(array1);

        System.out.printf("Values in array2 by row are%n");
        outputArray(array2);
    }

    public static void outputArray(int[][] array) {
        for(int row = 0; row < array.length; row++) {
            for(int column = 0; column < array[row].length; column++) {
                System.out.printf("%d  ", array[row][column]);
            }
            System.out.println();
        }
    }

}
