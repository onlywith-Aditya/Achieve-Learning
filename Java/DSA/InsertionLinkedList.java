public class InsertionLinkedList {
    public static void main(String []args){
        LinkedList_Insertion nums = new LinkedList_Insertion();
        nums.add(10);
        nums.add(20);
        nums.add(30);
        nums.add(40);

        nums.printValue();

        nums.addFirst(0);

        nums.printValue();

        nums.delete(20);

        nums.printValue();


    }
}
