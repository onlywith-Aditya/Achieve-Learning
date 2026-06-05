
public class Tree_Inbuild {
    public static void main(String []args){
        BinaryTree tree = new BinaryTree();
        tree.insert(50);
        tree.insert(40);
        tree.insert(60);
        tree.insert(30);
        tree.insert(70);
        tree.insert(20);
        tree.insert(80);
        tree.insert(10);
        tree.insert(90);
        tree.insert(0);
        tree.insert(100);

        tree.inOrder(); 
        System.out.println();
        tree.preOrder();
        System.out.println();
        tree.postOrder();

    }
}
