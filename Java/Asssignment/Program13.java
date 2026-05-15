// Write a program to perform the matrix addition & multiplication by allocation memory for an array dynamically.

public class Program13 {
    public static void main(String []args){
        
    }
}

// # 🔥 PROGRAM 16

// ### Matrix Addition & Multiplication

// ---

// ### ✅ Code

// ```java
// class Program16 {
//     public static void main(String[] args) {
//         int a[][] = {{1, 2}, {3, 4}};
//         int b[][] = {{5, 6}, {7, 8}};
//         int sum[][] = new int[2][2];
//         int mul[][] = new int[2][2];

//         // Addition
//         for (int i = 0; i < 2; i++) {
//             for (int j = 0; j < 2; j++) {
//                 sum[i][j] = a[i][j] + b[i][j];
//             }
//         }

//         // Multiplication
//         for (int i = 0; i < 2; i++) {
//             for (int j = 0; j < 2; j++) {
//                 for (int k = 0; k < 2; k++) {
//                     mul[i][j] += a[i][k] * b[k][j];
//                 }
//             }
//         }

//         System.out.println("Matrix Addition:");
//         for (int[] row : sum) {
//             for (int val : row)
//                 System.out.print(val + " ");
//             System.out.println();
//         }

//         System.out.println("Matrix Multiplication:");
//         for (int[] row : mul) {
//             for (int val : row)
//                 System.out.print(val + " ");
//             System.out.println();
//         }
//     }
// }
// ```

// ## 💡 Insight

// * Triple loop = multiplication logic
// * Most students panic here → you won’t

// ---

// # 🔥 PROGRAM 17

// ### Grade System

// ---

// ### ✅ Code

// ```java
// class Program17 {
//     public static void main(String[] args) {
//         int marks = 65;

//         if (marks >= 60)
//             System.out.println("First Class");
//         else if (marks >= 50)
//             System.out.println("Second Class");
//         else if (marks >= 40)
//             System.out.println("Pass");
//         else
//             System.out.println("Fail");
//     }
// }
// ```

// ---

// # 🔥 PROGRAM 18

// ### Leap Year

// ---

// ### ✅ Code

// ```java
// class Program18 {
//     public static void main(String[] args) {
//         int year = 2024;

//         if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
//             System.out.println("Leap Year");
//         else
//             System.out.println("Not a Leap Year");
//     }
// }
// ```

// ## 💡 Insight (IMPORTANT)

// Most people remember wrong logic. Correct rule:

// ```
// Divisible by 4 → leap
// BUT divisible by 100 → NOT leap
// BUT divisible by 400 → leap again
// ```

// ---

// # 🔥 PROGRAM 19

// ### Word Occurrence in String

// ---

// ### ✅ Code

// ```java
// import java.util.HashMap;

// class Program19 {
//     public static void main(String[] args) {
//         String str = "java is fun and java is powerful";
//         String words[] = str.split(" ");

//         HashMap<String, Integer> map = new HashMap<>();

//         for (String word : words) {
//             map.put(word, map.getOrDefault(word, 0) + 1);
//         }

//         System.out.println(map);
//     }
// }
// ```

// ## 💡 Insight

// * This is **interview-level logic**
// * HashMap = frequency counter

// ---

// # 🔥 PROGRAM 20

// ### Bank System using Switch

// ---

// ### ✅ Code

// ```java
// import java.util.Scanner;

// class Program20 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         double balance = 1000;
//         int choice;

//         do {
//             System.out.println("\n1.Deposit\n2.Display\n3.Withdraw\n4.Exit");
//             choice = sc.nextInt();

//             switch (choice) {
//                 case 1:
//                     System.out.print("Enter amount: ");
//                     double deposit = sc.nextDouble();
//                     balance += deposit;
//                     break;

//                 case 2:
//                     System.out.println("Balance: " + balance);
//                     break;

//                 case 3:
//                     System.out.print("Enter amount: ");
//                     double withdraw = sc.nextDouble();
//                     if (withdraw <= balance)
//                         balance -= withdraw;
//                     else
//                         System.out.println("Insufficient balance");
//                     break;

//                 case 4:
//                     System.out.println("Exit");
//                     break;
//             }
//         } while (choice != 4);
//     }
// }
// ```