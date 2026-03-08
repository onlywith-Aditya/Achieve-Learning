//Super-> Every Constructors in java has  this method super() by default.


// Inheritance

//class A{
class A  extends Object{

    public A(){
        // Calling constructor of Object Class.
        // Every  class in java call object class.
        // class A exten Object{}

        super(); 
        
        System.out.println("In 'A'");
    }
    // Parameterized Const.
    public A(int n){
        super();
        System.out.println("In 'A' int");
    }

}

class B extends A{

    public B(){
        
        super();
        System.out.println("In 'B'");
    }
    // Parameterized Const.
    public B(int n){
        //super();

        // This keyword
        this(); //-> Execute constructor of same class

        System.out.println("In 'B' int");
    }

}


public class this_super {
    public static void main(String[] args) {
        // So we are creating object of B and in that we are calling only B but A is also called.

        // Output-> 1 [In 'A' int and In 'B' int]
        // B obj = new B(5);

        
        // Output-> 2 [In 'A'  and In 'B']
        // B obj = new B();

        
        // Output-> 3 [In 'A' int and In 'B']
        //B obj = new B();

        // Output-> 4 [In 'A' and In 'B' and In 'B' Int] => Using this keyword
        B obj  = new B(5);

    }
    
}
