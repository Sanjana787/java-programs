import java.util.*;
public class Cb {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int j=0;
        System.out.print("Enter number :: ");
        int num=sc.nextInt();
        for( int i=2;i<num;i++){
            if(num%i!=0){
                continue;
            }
            // System.out.println(i+"\n");
             if(i*i==num){
                j=i;
                break;
             }
        }
        System.out.println(j);
    }
}
