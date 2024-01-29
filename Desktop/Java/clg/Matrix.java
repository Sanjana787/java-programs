import java.io.*;
import java.io.BufferedReader;

public class Matrix {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("enter array size ::");
        int n = Integer.parseInt(br.readLine());
        int arr[][] = new int[n][n];
        int b[][] = new int[n][n];
        int sum[][] = new int[n][n];
        System.out.println("enter array elements::");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(br.readLine());
            }
        }
        System.out.println("enter array elements::");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                b[i][j] = Integer.parseInt(br.readLine());
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sum[i][j] = arr[i][j] + b[i][j];
            }
        }
        System.out.println("Sum of given Arrays");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(sum[i][j] + " ");
            }
            System.out.println();
        }
    }
}
