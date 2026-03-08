// Method_Overriding-> It is process in which we used  same method name in inherit  class.

class Calc{
    public int add(int a, int b){
        System.out.println("Calc");
        return a+b;
    }
}

class AdvCalc extends Calc{
    public int add(int a, int b){
        System.out.println("AdvCalc");
        return a+b;
    }
}


public class Method_Overriding {
    public static void main(String[] args) {

        AdvCalc c = new AdvCalc();
        System.out.println(c.add(2,3));
    
    }
}
