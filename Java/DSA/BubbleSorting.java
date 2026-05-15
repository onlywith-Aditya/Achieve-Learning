public class BubbleSorting {
    
    public static void main(String args[]){
            int nums[] = {6,5,2,7,8,4};

            System.out.println("Before Sorting");
            for(int num :  nums){
                System.out.print(num + " ");
            }

            // Bubble Sort
            int temp = 0;

            for(int i=0;i<nums.length;i++)
                {
                for(int j = 0;j<nums.length-1;j++)
                    {
                    if(nums[j] > nums[j+1])
                        {
                        temp =  nums[j];
                        nums[j] = nums[j+1];
                        nums[j+1] = temp;
                    }
                }
                System.out.println();
                for(int num :  nums){
                    System.out.print(num + " ");
                }
            }
            System.out.println();
            System.out.print("After Sorting");
            System.out.println();
                for(int num :  nums){
                    System.out.print(num + " ");
                }
    }

}
