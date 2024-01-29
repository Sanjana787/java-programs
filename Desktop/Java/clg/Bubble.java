import java.io.BufferedReader;
import java.io.*;
public class Bubble{
    public static void bubble(int a[],int n){
        for(int i=0;i<n;i++){
            for(int j=0;j<n-1;j++){
                if(a[j]>a[j+1]){
                    int temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        System.out.println("enter size of array::");
        int size=Integer.parseInt(br.readLine());
        int arr[]=new int[size];
        System.out.println("enter array elements ::");
        for(int i=0;i<size;i++){
          arr[i]=Integer.parseInt(br.readLine());
        }
        bubble(arr,size);
        System.out.println("Array elements after sorting::");
        for(int i :arr){
            System.out.println(i);
        }
    }
}