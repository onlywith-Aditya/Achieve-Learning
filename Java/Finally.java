import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;




public class Finally {
    public static void main(String []args){

        // We will take input from user.
        // Then we will try to handle exception.
        // Then we close the resource.

        // int num = 0;
        // BufferedReader bf = null;
        // try{
        //     //InputStreamReader in = new InputStreamReader(System.in);
        //     bf = new BufferedReader(new InputStreamReader(System.in));
        //     num = Integer.parseInt(bf.readLine());
        //     System.out.println(num);


        // }
        
        // catch(Exception e){
        //     System.out.println("Exception: " + e);
        // }
        // finally{
        //     System.out.println("Byeee!!");
        //     try {
        //         bf.close();
        //     } catch (IOException e) {
        //         e.printStackTrace();
        //     }
        // }
        

        // Method-2-----------|
            // Auto Close.

        int  num = 0;
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){

            num = Integer.parseInt(br.readLine());
            System.out.println(num);

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
