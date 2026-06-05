// class Node{
//     int data;   
//     Node next;

//     public Node(int data){
//         this.data = data;
//         next = null;
//     }

// }

// public class LinkedList{

//         // Heading Head
//         Node head  = null;

//     public void add(int data){
//         Node newNode = new Node(data);
//         //newNode.data = data; // We are not using this line because we already initialize this in constructor of Node.

//         // This variable is used to track the current variable.
//         Node current = head;


//         if(head == null){
//             head = newNode;
//         }
//         else{
//             while (current.next!=null) {
//                 current = current.next;
//             }
//             current.next = newNode;
//         }

//     }

//     public void printValues(){
//         Node current = head;
//         while(current!=null){
//             System.out.print(current.data + "->");
//             current = current.next;
//         }
//         System.out.print("NULL");
//     }


// }
