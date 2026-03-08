
interface First{

    String city = "Mumbai"; 
    
    void show();
    void config();

}

interface Second{
    void run();
}


class Last implements First, Second{ // Implments about interfaces.

    public void show(){
        System.out.println("Show");
    }
    public void config(){
        System.out.println("Configure");
    }
    public void run(){
        System.out.println("Run");
    }

}


public class Interface_Mulitple {
    public static void main(String[] args) {
        First a  = new Last();
        a.config();
        a.show();
        // a.run(); -> This cannot use,because First don't know about Second.
        
        Second b = new Last();
        b.run();

    }
}
