import java.lang.*;
import java.util.*;
public class LeapY {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a Year");
        int year=sc.nextInt();
        if(year%4==0&& year%100!=0){
           System.out.println("Its a leap year!!");
        }
        else if (year%100==0&&year%400==0){
           System.out.println("Its a leap year!!");
               
            }
        else{
             System.out.println("Its not a leap year!!");
        }
    }
}
