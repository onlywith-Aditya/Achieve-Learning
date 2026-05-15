//Write a program to perform addition of n numbers, by taking inputs from command line arguments.

public class Program4 {
    public static void main(String []args){
    
        int x = Integer.parseInt(args[0]);
        int sum = 0;
        for(int i = 0 ; i<=x;i++){

            sum +=i; 
        }

        System.out.println("Sum of N number is: " + sum);

    }    
}
