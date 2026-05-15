// Write a program to compute & print factorial of any given number.

public class Program5{
    public static void main(String []args){
        int x = Integer.parseInt(args[0]);
        int fact = 1;
        for(int i =1;i<=x ; i++){
            fact *= i;
        }

        System.out.println("Factorial of Number is :" + fact);

    }
}