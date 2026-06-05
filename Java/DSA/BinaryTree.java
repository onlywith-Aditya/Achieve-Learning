class Node{
    //data
    //left node
    //right node
    int data;
    Node left;
    Node right;

    public Node(int data){
        this.data = data;
    }
}

public class BinaryTree {
    // Root Node
    Node root;

    public void insert(int data){
        root = insertRec(root,data);
    }
    
    // Insertion in tree.
    public Node insertRec(Node root, int data){
        // Check new node, if it is not root node.
        if(root == null){
            root = new Node(data);
        }
        else if(data < root.data){
            root.left = insertRec(root.left, data);
        }
        else if(data > root.data){
            root.right = insertRec(root.right,data);
        }
        return root;
    }

    // Print and Traversal Tree_Inbuild
        // InOrder
        // PreOrder
        // PostOrder


    // InOrder
    public void inOrder(){
        inorderRec(root);
    }
    public void inorderRec(Node root){
        if(root != null){
            inorderRec(root.left);
            System.out.print(root.data + " "); //Root.
            inorderRec(root.right);
            
        }
    }

    //PreOrder
    public void preOrder(){
        postorderRec(root);
    }
    public void preorderRec(Node root){
        if(root != null){

            System.out.print(root.data + " "); // Root.
            preorderRec(root.left);
            preorderRec(root.right);
            
        }
    }

    //PostOrder
    public void postOrder(){
        postorderRec(root);
    }
    public void postorderRec(Node root){
        if(root != null){

            
            postorderRec(root.right);
            postorderRec(root.left);
            System.out.print(root.data + " "); // Root.
            
        }
    }

}
