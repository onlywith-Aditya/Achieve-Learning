import java.lang.Thread;



// class A implements Runnable
class A extends Thread{
    public void run(){
        for(int i = 0;i<=100;i++){
            System.out.println("Hi");
            try{
                Thread.sleep(10);
            }
            catch(InterruptedException e){
                e.printStackTrace();
            }
            
        }
    }
}
class B extends Thread  {
    public void run(){
        for(int i = 0;i<=100;i++){
            System.out.println("Hello");
            try{
                Thread.sleep(10);
            }
            catch(InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}


class threads{
    public static void main(String args[]){

        A obj1 = new A();
        B obj2 = new B();

        // obj2.setPriority(Thread.MAX_PRIORITY);
        // System.out.println(obj1.getPriority());

        // Runnable method is not working with start(), for that we have to make reference varibles of thread.
            
            // Runnable obj1 = new A();''
            // Thead t1 = new Thread(obj1);
            //  t1.start();

        
        obj1.show();
        obj2.show();
        obj1.start();
        try{
                Thread.sleep(20);
            }
            catch(InterruptedException e){
                e.printStackTrace();
            }
        obj2.start();


    }
}