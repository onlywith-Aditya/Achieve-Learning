// Write a program to compute the sum of digits of a given Integer.

public class Program6 {
    public static void main(String[] args) {
        int x = 12345;
        int sum = 0;
        
        while( x > 0){
            sum += x % 10;
            x = x / 10;
        }
        System.out.println("Sum of digits are: " + sum);
    }
}
