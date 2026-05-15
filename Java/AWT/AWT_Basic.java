import java.awt.*;

public class AWT_Basic{
    public static void main(String args[]){
        Frame f = new Frame("Application");

        Button btn = new Button("Click ME");
        Label lbl = new Label("Enter Name:");
        TextField tf = new TextField(20);
        
        f.setLayout(new FlowLayout());
        f.add(lbl);
        f.add(tf);
        f.add(btn);
        
        f.setSize(400,300);
        f.setVisible(true);
    } 
}