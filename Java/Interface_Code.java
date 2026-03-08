
interface A{

    // All variables are final and static.
    
    int age = 55;   // Final and Static.
    // Static we can directyl access it.
    String city = "Mumbai"; 
    
    void show();
    void config();

}

class B implements A{

    public void show(){
        System.out.println("Show");
    }
    public void config(){
        System.out.println("Configure");
    }

}

public class Interface_Code {
public static void main(String []args){

    // B b = new B();
    // b.show();
    // b.config();

    A obj  = new B();
    obj.show();
    obj.config();
    
    // Access variable of interface.
    System.out.println(A.city);


}  

}

