package lambert.simple;

public class EvenNumbers {
    public static void main(String[] args) {
        int count = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 2 == 0) {
                System.out.println(i);
                count++;
            }
        }
        System.out.println("Total count of even numbers: " + count);
    }
}


/*Problem 1: Print Even Numbers

Write a Java program that prints all even numbers from 1 to 100 using a for loop.*/
