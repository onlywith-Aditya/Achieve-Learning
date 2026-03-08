// Method Overloading-> When different method of same name and are used in one/self class.

class Calculator_Overloading{
        

    // Creating different method of same name but different arguments.
    public int add(int n1, int n2){
        return n1+n2;
    }
    public int add(int n1,int n2,int n3){ // This are local variable.
        return n1+n2+n3;
    }
    public double add(double n1,double n2,double n3){
        return n1+n2+n3;
    }
    public int add(int n1,int n2,int n3,int n4){
        return n1+n2+n3+n4;
    }


}



public class Method_Overlaoding_3 {
    
    public static void main(String args[]){

        int n1 = 2;
        int n2 = 4;
        int n3 = 6;
        int n4 = 8;
        
        // Calling method
        Calculator_Overloading calc = new Calculator_Overloading();
        
        // Int Type
        int result = calc.add(n1, n2, n4);
        System.out.println(result);

        
        // Double Type
        double result_1 = calc.add(2.5, 2.5, 2.5);
        System.out.println(result_1);

    }
}
