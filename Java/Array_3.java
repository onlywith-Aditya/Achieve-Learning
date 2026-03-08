// Jagged Array
// Array's of Array-> Multi-Dimension Array.

public class Array_3 {
    public static void main(String args[]){

        // Columns sized is not fixed, individual columns has there size mention.

        // Different rows of same size have different size columns.
        int arr[][] = new int[3][];
        arr[0] =  new int[3];
        arr[1] = new int[4];
        arr[2] = new int[5];
    
        // For size of array.
            for (int i = 0;i<arr.length;i++){
                for (int j = 0; j<arr.length;j++){
                    arr[i][j]=(int)(Math.random()*10);
                }
            }

            // In this we don't have to mention size. 
            // for (int n[]:arr){
            //     for (int m:n){
            //         System.out.print(m + " ");
            //     }
            //     System.out.println();
            // }





    }
}

