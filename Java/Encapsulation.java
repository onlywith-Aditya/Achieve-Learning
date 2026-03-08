// Encapsulation-> Hiding necessary data.
// We used this keyword when we have to used both instance and local variable of same name.

class Human
{
        // It is restricted not one from out side world can access it directly. 
    private int age = 22;
    private String name = "Aditya";
    private int bank_number;
    private int age_2;


    public int getAge(){
        return age;
    }

    public String getName(){
        return name;
    }

    public int getBank(int bank){
        bank_number = bank;
        return bank_number;
    }
        // FIXED: Changed method name and made it a proper setter
    public void setAge_2(int age_2){
        // this keyword represent current object.
        this.age_2 = age_2;
    }

    // ADDED: Getter for age_2
    public int getAge_2(){
        return age_2;
    }

}

public class Encapsulation 
{
    public static void main(String[] args) 
    {
        Human obj = new Human();
        System.out.println(obj.getName() + obj.getAge());
        System.out.println(obj.getBank(20000));

         // FIXED: First set, then get
        obj.setAge_2(50);                       // Set the value
        System.out.println(obj.getAge_2());      // Get and print the value
    }
}
