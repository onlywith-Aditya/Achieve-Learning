// Method Overriding.
// In case of difference between expected output and real output is called BUGS.
// To handle BUGS we use annotation mean tell compiler that this is siutation and tell me if arise.

// @Override | @Deprecated and etc.

class A{
    
    // Change method name from show() to newShowTheDataWhichBelongsToThisClass()
    public void newShowTheDataWhichBelongsToThisClass(){
        System.out.println("In A Show");
    }




}
class B extends A{
    @Override
    public void newShowTheDataWhichBelongsToThisClass(){
        System.out.println("In B Show");
    }

}


public class Annotatiion {
public static void main(String[] args) {
    B obj = new B();
    obj.newShowTheDataWhichBelongsToThisClass();
}   
}
