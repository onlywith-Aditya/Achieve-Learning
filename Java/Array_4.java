// Array of Object.

class Students{
    // Instance Variable.

    long rollnumber;
    String name;
    int marks;
}

public class Array_4{
    public static void main(String args[]){

        // Objects of Students.
        
        Students s1 = new Students();
            s1.rollnumber = 2502030071L;
            s1.name = "Aditya";
            s1.marks = 90;

        Students s2 = new Students();
            s2.rollnumber = 2502030067L;
            s2.name = "Harsh";
            s2.marks = 80;
            
        Students s3 = new Students();
            s3.rollnumber = 2502030000L;
            s3.name = "Sourabh";
            s3.marks = 70;

        // Array of Objects.
        Students students[] = new Students[3];
        students[0] = s1;
        students[1] = s2;
        students[2] = s3;

        // for(int i=0; i< 3; i++){
        //     System.out.println(students[i].name + "\n" + students[i].rollnumber + "\n" + students[i].marks);
        // }

        

    //------------------Enhance-For-Each------> Don't used counter.
        for (Students stud :students){
            System.out.println(stud.name + ":" + stud.rollnumber + ":" + stud.marks);
        }

    }
}
