// Observation->
    // It call constuctor two times.
    // And Static block only one time.
    // And also  it execute static first.


class Mobile_Const{ 

    static String name; 
    int price;
    String brand;


    // Constructor
    public Mobile_Const(){
        // Default things.
        brand = "";
        price = 200;

        //name = "Phone"; 

        // This is initialize every time and if we want to initialize only once.

        System.out.println("Inside Constructor Block");
        
    }


    static{ // It call only once.
        name = "Phone";
        System.out.println("Inside Static Block");
    }


    public void disp(){
        System.out.println(name+ ":" + brand + "-> "+ price);
    }

}


public class Static_block
{

    public static void main(String args[]) throws ClassNotFoundException
    {


        Class.forName("Mobile_Const");


        // Mobile_Const obj1 = new Mobile_Const();
        // obj1.brand = "Apple";
        // obj1.price = 2000;
        // Mobile_Const.name = "Smartphone";
        
        // Mobile_Const obj2 = new Mobile_Const();



    }
}