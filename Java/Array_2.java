// Array's of Array-> Multi-Dimension Array.

public class Array_2 {
    public static void main(String args[]){

        int arr[][] = new int[3][3];

        // Assign Elements
        for (int i = 0;i<3;i++){
            for (int j = 0; j<3;j++){
                 // Random Values in Java.
                arr[i][j]=(int)(Math.random()*10);
            }
        }

        
        // Access Elements-> 1.
            // for (int i = 0;i<3;i++){
            //     for (int j = 0; j<3;j++){
            //         System.out.print(arr[i][j] + " ");
            //     }
            // System.out.println();
            // }


        // Access Elements-> 2.
            for (int n[]:arr){
                for (int m:n){
                    System.out.print(m + " ");
                }
                System.out.println();
            }



    }
}
