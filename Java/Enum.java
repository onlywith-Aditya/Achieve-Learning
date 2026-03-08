
enum Week{
    Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday, Sunday;
}


public class Enum {
    public static void main(String []args){
        Week w = Week.Wednesday;
        System.out.println(w);
        // Every enum is a assign a number, so in java it start with 0.
        System.out.println(w.ordinal());
        // If you want to get all status of Enum.
        Week[] week = Week.values(); // Gives you an array.
        for(Week x: week){
            System.out.println(x + " : " + x.ordinal());
        }
        
    }
}
