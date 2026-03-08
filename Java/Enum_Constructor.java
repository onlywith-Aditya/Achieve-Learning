enum Laptop{
    Macbook(1300), CPS(2300), Surface(2400), Thinkpad(2000);
    // This is constuctor Laptop with price.
    private int price;
    
    private Laptop(int price){
        this.price  = price;
    }

    public int getPrice(){
        return price;
    }
    
    public void setPrice(int price){
        this.price =  price;
    }
    
    
}


public class Enum_Constructor {
    public static void main(String []args){

        Laptop lap = Laptop.Macbook;
        
        for(Laptop x: Laptop.values()){
            System.out.println("Brand: " + x + ", Price: " + x.getPrice());
        }


        // To access price of enum we have to access with getter and setter.    

    }
}
