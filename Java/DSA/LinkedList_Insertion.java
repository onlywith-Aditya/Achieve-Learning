class Node {  // Uppercase class name
    int data;
    Node next;
    
    public Node(int data) {
        this.data = data;
        next = null;
    }
}


public class LinkedList_Insertion{
    Node head = null;

    // Add {Node}
    public void add(int data) {
        Node newNode = new Node(data);  
        Node current = head;
        
        if(current == null) {
            head = newNode; 
        } else {
            while(current.next != null) {
                current = current.next;
            }
            current.next = newNode;  
        }
    }

    // Add {Print}
    public void printValue(){
        Node current  = head;
        while(current!=null){
            System.out.print(current.data + "->");
            current = current.next;
        }
        System.out.println("NULL");

    }

    // Insertion at Beginning
    public void addFirst(int data){
        // Create new node.
        Node newNode = new Node(data);
        newNode.next = head;
        // Replace current
        head = newNode;
    }

    // Delete Element
    public void delete(int data){
        // Firsa traversal to find node.
        Node current  = head;
        while(current!=null && current.next.data!=data){
            current = current.next;
        }
        if(current.next != null){
            current.next = current.next.next;
        }
    }
}