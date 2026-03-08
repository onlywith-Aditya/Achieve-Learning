
class Calculator{  // Class

    // Variable
    int a = 5;


    // Method
    public int add(){
        System.out.println("Add");
        return 0;
    }
}


public class Class_Object_1 {

    public static void main(String args[]){

    int a  = 5;
    int b = 6;

    System.out.println("A+B:"+ a+b);

    //Call Add() Method-> Instace of Class.


            //Calculator calc; // Refence of Class.


            // Create Object of Class.
            Calculator calc = new Calculator();
            int result  = calc.add();// You can also pass parameters.

            System.out.println("Value in Object: " + result);

            // This object also return somethings.



    }
}