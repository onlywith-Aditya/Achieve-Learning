// StringBuffer-> Mutuable String

public class String_Buffer {
    public static void main(String[] args) {
        
        // StingBuffer give size of 16 bits.
        StringBuffer sb = new StringBuffer("Aditya"); // It will show 22 why it keep 16 in buffer in case of if now extra memory for allocation then it will used thjis 16 buffer memory,
        System.out.println(sb.capacity()); 

        // Append Data
        sb.append(" Dadhich");
        System.out.println(sb); 

        // To convert StringBuffer into String we can used toString() method

        String str = sb.toString();
        System.out.println(str); 



    }
}
