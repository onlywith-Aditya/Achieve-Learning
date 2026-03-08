

public class Exception_Handling {
    public static void main(String []args){

        // Exception Handling in case of denomanitor is '0'.

        int i = 2;
        int  j = 0;

        int arr[] = new int[5];

        try
        {
            j = 18/i; // It throw-> Arithemtic Excepetion Error.
            System.out.println(arr[0]);
            System.out.println(arr[5]); // Out of bound Exception,.

        }
        catch(ArithmeticException e)
        {
                //Warning and print exception.
            System.out.println("Went wrong!!!" + e);
        }
        catch(ArrayIndexOutOfBoundsException e)
        {
            //Warning and print exception.
            System.out.println("Stay in limit!!!" + e);
            
        }
        catch(Exception e)
        {
            System.out.println("Something went wrong!!!!" + e);
        }

        System.out.println(j + " \n " + "Bye!!!");

    }
}
