

class AdiException extends Exception{
    public AdiException(String string){
        super(string);
    }
}


public class Throw {
    public static void main(String []args){

        // Exception Handling in case of denomanitor is '0'.


        // ->> I want if someone try to divide number by '0', it handles by divide the number by '1'.

        int i = 20;
        int  j = 0;

        try
        {
            j = 18/i;   
            if(j==0)

            // System Exception
                throw new ArithmeticException("Not Allow to divide by '0'");

            //  My Own Exception-> AdiException
                throw new AdiException("This is my Exception");



        }
        catch(AdiException e){
            System.out.println("This is not allow to do!!!. [Bye AdiException] \n" + e);
        }   
        catch(ArithmeticException e)
        {
            j = 18/1;
            System.out.println("No 0 it's default value 1[System Exception]\n" + e);
        }
        catch(Exception e)
        {
            System.out.println("Something went wrong!!!!" + e);
        }

        System.out.println(j + " \n " + "Exit!!!");

    }
}
