// Observation->
    // It call constuctor two times.
    // And Static block only one time.
    // And also  it execute static first.


class Mobile_Method{ 
    String brand;
    int price;
    static String name;

    public void show(){
        System.out.println(name+ ":" + brand + "-> "+ price);
    }

    // Create static method-> Object Reference.
    public static void show1(Mobile_Method obj1){
        System.out.println("In Static Method");

        // We can use static instance variable in static method, but we can't use non-static instancer variable in static method.

        System.out.println(name+ ":" + obj1.brand + "-> "+ obj1.price);
        
        // To get non-static instance variable we have to pass it as arguments/ reference.

        
    }

}


public class Static_Method
{

    public static void main(String args[]) 
    {



        Mobile_Method obj1 = new Mobile_Method();
        obj1.brand = "Apple";
        obj1.price = 2000;
        Mobile_Method.name = "Smartphone";
        
        Mobile_Method obj2 = new Mobile_Method();

        // We can't use it-> 
            //Mobile_Method.show();

        // We can use it->
            Mobile_Method.show1(obj1);
        


    }
}