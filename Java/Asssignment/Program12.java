// Write a program to sort the element in an array.

// import java.util.Arrays;

public class Program12 {    
    public static void main(String []args){
        int arr[] = {5,4,3,2,1};

        // Do in manual way.->Bubbel Way.
        for(int i = 0; i< arr.length-1; i++){
            for(int j = 0; j< arr.length-1; j++){
                if(arr[j] > arr[j+1]){
                    //Swap
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
            // Print sorted array
        System.out.println("Sorted Array:");
        for(int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    }

