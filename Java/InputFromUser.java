import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class InputFromUser {
    public static void main(String []args){

        // Print 
        System.out.println("Enter your number: ");

        // Method 1st-> ASCII Value
        
        // int num = 0;
        // try {
        //     num = System.in.read();
        // } catch (IOException e) {
        //     e.printStackTrace();
        // }
        // finally{
        //     System.out.println("Number: " + num);
        // }


        // Method 2nd-> BufferedReader

        // InputStreamReader in = new InputStreamReader(System.in);
        // BufferedReader bf = new BufferedReader(in);

        // // bf.readLine()-> Give String.
        // int num = 0;

        // try {
        //     num = Integer.parseInt(bf.readLine());
        // } 
        // catch (NumberFormatException | IOException e) {
        //     e.printStackTrace();
        // }

        // System.out.println("Number-2 : " + num);

        // //bf.close(); // Not mendatory but prefered.


        // Method 3rd-> Scanner(java.util.Scanner)
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        System.out.println("Number: " + num);

        sc.close(); // Closing Resource.

    }
}
