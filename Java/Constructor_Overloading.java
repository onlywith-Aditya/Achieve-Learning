// Creating multiple Constructor with different Parameter.

class HUman{
    private int age;
    private String name;

    // Types of Constructor

    public HUman(){ // Default Constructor
        age = 25;
        name = "Bhavesh";
    }

    public HUman(int a, String b){ // Parameterized Constructor
        age = a;
        name = b;
    }


    public int getAge(){
        return age;
    }
    public void setAge(int age){
        this.age = age;
    }
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }

}

public class Constructor_Overloading {
    public static void main(String[] args) {
        
        HUman hm = new HUman();
        HUman hm1 = new HUman(20,"Rahul");
        System.out.println(hm.getAge());
        System.out.println(hm.getName());
        System.out.println(hm1.getAge());
        System.out.println(hm1.getName());


    }
}
