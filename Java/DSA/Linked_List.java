import java.util.LinkedList;


public class Linked_List {
    public static void main(String []args){

        // Create object of Linked List which is of type Integer.
        LinkedList<Integer> nums = new LinkedList<>();
        nums.add(5);
        nums.add(6);
        nums.add(7);

        nums.addFirst(4);
        System.out.println(nums);

        System.out.println(nums.peek());
        

    }
}
