import java.io.*;
import java.util.Arrays;
public class Matrix_rec {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        System.out.println("enter rows and columns of matrix::");
        int row=Integer.parseInt(br.readLine());
        int col=Integer.parseInt(br.readLine());
        int arr[][]=new int [row][col];
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                arr[i][j]=Integer.parseInt(br.readLine());            }
        }
        System.out.println("Transpose of the given matrix::");
        for(int i=0;i<col;i++){
            for(int j=0;j<row;j++){
                System.out.print((arr[i][j]));
           }
        }
    }
    
}
