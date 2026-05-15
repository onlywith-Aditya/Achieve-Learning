// Write a program to reverse the digits of a numbers.

public class Program8 {
    public static void main(String []args){
        int num = 12345;
        int reverse = 0;
        while(num>0){
            reverse = reverse * 10 + num % 10;
            num  = num/10;
        }
        System.out.println("Reverse: " + reverse);
    }
}
