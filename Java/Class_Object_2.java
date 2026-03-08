// Creating class
class Computer{

        // Method-1.
    public void playBack(){
        System.out.println("Music Playing");
    }


        // Method-2.
    public String getMePen(int cost){
            // NO use of cost variable.
        return "Pen";
    }
    
}

public class Class_Object_2 {
    public static void main(String args[]){

        // Call Method 1.
        Computer obj = new Computer();
            // obj->  Refence Variable.
        
            obj.playBack();
            String str = obj.getMePen(2);

            // Print str.
            System.out.println(str);

    }
}
