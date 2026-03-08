// SAM or Functional Interface-> Only one method in it.

@FunctionalInterface  // Annotation of SAM Interface.
interface Single{
    void show(int i, int j);
}


public class Type_Interfaces {
    public static void main(String [] args){

        // Instead of creating another class we can use and initiated own A interface class.
                    // Single obj = new Single(){      // This is called Annoymous Class.
                    //     public void show(){
                    //         System.out.println("In Show");
                    //     }
                    // };

                    // obj.show();
    
        // Lambda Expression(->)

        Single obj = (i, j) -> System.out.println("In Show " + i + " " + j);
    
        obj.show(4,5);
        
    }
}
