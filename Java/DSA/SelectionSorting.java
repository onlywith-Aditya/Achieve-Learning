public class SelectionSorting{
    
    public static void main(String args[]){
            int nums[] = {6,5,2,7,8,4};
            int size = nums.length;
            int temp = 0;

            System.out.println("Before Sorting");
            for(int num :  nums){
                System.out.print(num + " ");
            }

            // Selection Sorting
            int minIndex = -1;
            for(int i = 0 ;i<size -1; i++)
                {
                minIndex = i;
                    for(int j = i+1;j<size;j++)
                        {
                            if(nums[minIndex] > nums[j])
                                {
                                    minIndex = j;
                            }
                        }
                        // Swap
                        if(minIndex != i) {
                            temp = nums[minIndex];
                            nums[minIndex] = nums[i];
                            nums[i] = temp;
                            }

                        // Print Iteration
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

