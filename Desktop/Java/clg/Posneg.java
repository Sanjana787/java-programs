import java.util.*;
public class Posneg {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("enter a number::");
        int a=sc.nextInt();
        if(a==0){
            System.out.println("Entered number is zero");
        }else if(a>0){
            System.out.println("Entered number is positive");
        }else{
            System.out.println("Entered number is negative");
        }
    }
}
