public class Searching{
public static void main(String[] args) {
    int nums[] = {1,2,3,4,5,6};
    int target  = 5;

    int result1 = LinearSearch(nums, target);
    int result2 = BinarySearch(nums, target, 0, nums.length-1);
    if(result1 != -1){
        System.out.println("Element found at Index: " + result1);
    }
}

public static int LinearSearch(int[] nums, int target) {
    int steps = 0;
    for(int i = 0 ; i<nums.length;i++){
        steps ++;
        if(nums[i] == target){
            System.out.println("Steps By LInear Seach: " + steps);
            return i;
        }
    }
    return -1;
}

public static int BinarySearch(int[] nums, int target, int  left, int right) {


      // Recursion Code-------------------|
        if(left <= right){
            int mid = (left + right)/2;
            if(nums[mid] == target){
                return mid;
            } 
            else if(nums[mid] < target){
            return BinarySearch(nums , target, mid + 1, right);
            }
            else{
                return BinarySearch(nums, target, left, mid - 1);
            }
        }




        return -1;

    // int steps = 0;
    // int left = 0;
    // int right = nums.length - 1;


    // while(left<=right){
    //     steps ++;
    //     int mid = (left + right) /2;
    //     if(nums[mid] == target ){
    //         System.out.println("Steps in BinarySearch: " + steps);
    //         return mid;
    //     }
    //     else if(nums[mid] <= target){
    //         left = mid + 1;
    //     }
    //     else{
    //         right =  mid - 1;
    //     }
    // }
    // System.out.println("Steps in BinarySearch: " + steps);
    // return -1;
}
}