import java.util.*;

public class Collection_exp {
    public static void main(String[] args) {

        // Collection<Integer>  nums = new ArrayList<Integer>();

        List<Integer> nums = new ArrayList<Integer>();


        // ArrayList-> Extends Class "list", and it provide indexing.

        nums.add(1);
        nums.add(2);
        nums.add(3);
        nums.add(4);
        nums.add(5);

        // indexing
        System.out.println("Indexing: " + nums.get(2));

        for(int n: nums){
            System.out.println(n);
        }


    }
}
