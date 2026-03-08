class HUman{
    private int age;
    private String name;

    public HUman(){

        // System.out.println("In Constructor");
        age = 25;
        name = "Bhavesh";

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

public class Constructor {
    public static void main(String[] args) {
        
        // Every time you create an object it call Constructor.

        HUman hm = new HUman();
        // Creating another  object.-> Constructor call two times.
        HUman hm1 = new HUman();
        // hm.setAge(20);
        // hm.setName("Aditya");
        System.out.println(hm.getAge());
        System.out.println(hm.getName());


    }
}
