import java.util.Scanner;

public class Rev {
     public static void main(String[] args) {
     Scanner sc=new Scanner(System.in);
     int i=0;
      System.out.print("Enter a number ::");
      int num=sc.nextInt();
      while(num>0){
         i=i*10; 
        i+=num%10;
        num=num/10;
       
      }
     System.out.print("Reverse of the number is::"+i);
   } 
}
