import java.io.*;
import java.io.BufferedReader;
public class Array1D {
    public static void main(String[] args)throws  Exception {
        BufferedReader br= new BufferedReader( new InputStreamReader(System.in));
   
        System.out.println("enter size::");
        int sum=0;
        int n=Integer.parseInt(br.readLine());
        int []arr=new int[n];
        System.out.println("enter array elements::");
        for(int i=0;i<n;i++){
          arr[i]=Integer.parseInt(br.readLine());
        }
        System.out.println("entered array elements are ::");
        for(int i :arr){
           System.out.println(i);
        }    
        for(int i :arr){
            sum+=i;
        }
        System.out.println("percent is::"+sum/n);
        
    }
}
