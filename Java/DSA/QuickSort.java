public class QuickSort 
{

    public static void QuickSort(int[] arr, int low, int high)
    {
        if(low<high)
        {
            int pi = partition(arr, low, high);
            QuickSort(arr,low,pi-1);
            QuickSort(arr,pi+1,high);
        }
    }

    private static int partition(int[] arr, int low, int high)
    {
        int pivot = arr[high];
        int i = low - 1;

        for(int j = low;j<high;j++){
            if(arr[j] < pivot){
                i++;
                // Inner Swap
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        // Outer Swap
        int temp = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = temp;

        return i+1;


    }

    public static void main(String  []args)
    {
        int arr[] = {5,6,2,3,1,8,4};

        // QuickSort
        QuickSort(arr, 0, arr.length-1);

        // Print Array
        for (int num : arr)
            {
            System.out.println(num + " ");
        }

    }   

}
