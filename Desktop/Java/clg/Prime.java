import java.util.Scanner;

public class Prime {
    public static int prime(int n){
        for(int i=2;i*i<n;i++){
            if(n%i!=0){
             return 0;
            }
            else {
                return 1;
            }
        }
     return 0;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int ans;
        System.out.println("enter a number::");
        int num=sc.nextInt();
       ans= prime(num);
       if(ans==0){
        System.out.print(num+" is a prime number");
       }
       else if(ans==1){
        System.out.println(num+" is not a prime number");
       }
    }
}
