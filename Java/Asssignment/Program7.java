// Write a program to calculate & p;rint first n Fibonacci numbers;

public class Program7 {
    public static void main(String []args){
        int n = 10;
        int a = 0;
        int b = 1;
        System.out.println(a + "\n" + b);
        for (int i = 2; i<n; i++){
            int c = a+b;
            System.out.println(c + " ");
            a = b;
            b = c;
        }

    }
}
