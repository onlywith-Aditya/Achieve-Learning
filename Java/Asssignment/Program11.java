// Write a program to show the scope and lifetime of a variables.

public class Program11 {    
    public static void main(String []args){
         int x = 10;  // local variable

        if (x > 5) {
            int y = 20;  // block scope
            System.out.println("Inside block: " + y);
        }

        // System.out.println(y); // ERROR (out of scope)
    }
}
