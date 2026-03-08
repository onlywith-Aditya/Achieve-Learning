
class Mobile_Static{  // Class

    // Instance variables.
    static String name;
    int price;
    String brand;

    public void disp(){
        System.out.println(name+ ":" + brand + "-> "+ price);
    }

}


public class Static_Demo {

    public static void main(String args[]){

        Mobile_Static obj1 = new Mobile_Static();
        obj1.brand = "Apple";
        obj1.price = 2000;
        obj1.name = "Phone"; // It gives warning that static filed should used static way.
        obj1.disp();

        Mobile_Static obj2 = new Mobile_Static();
        obj2.brand = "Samsung";
        obj2.price = 1500;
        //obj2.name = "Phone";
        // Correct way to use.
        Mobile_Static.name = "Phone";
        obj2.disp();


        // Try to change static variable.
        Mobile_Static.name ="Smartphone";
        obj1.disp(); // Obj of 1 is also change to smartphojne
        obj2.disp();



    }
}