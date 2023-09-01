// Driver code?

public class Apps {

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int x = 3;

        int index = bisectRight(arr, x);
        System.out.println(index); // 3

        arr = {1, 2, 3, 4, 5};
        int index = bisectLeft(arr, x);

        System.out.println(index); // 2
    }

}
