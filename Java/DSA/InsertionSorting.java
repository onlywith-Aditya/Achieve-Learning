public class InsertionSorting{
    
    public static void main(String args[]){
            int arr[] = {5,6,2,3,1};


            // Before Print
            System.out.println("Before Sorting");
            for(int num :  arr){
                System.out.print(num + " ");
            }

            // Insertion Sorting
            for (int i = 1 ;i<arr.length;i++){
                int key = arr[i];
                int j = i-1;
                while (j>= 0 && arr[j]>key) 
                    {
                        // Shifting
                        arr[j+1] = arr[j];
                        j--;
                    
                }
                arr[j+1] = key;

                // Print Every Step
                System.out.println();
                for(int num : arr){
                    System.out.print(num + " ");
                }
            }
            



            
            // After Print
            System.out.println();
            System.out.print("After Sorting");
            System.out.println();
                for(int num :  arr){
                    System.out.print(num + " ");
                }
    }
}

