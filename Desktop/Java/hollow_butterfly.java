public class hollow_butterfly {
    public static void main(String args[]){
        int n=10;
        for(int i=1;i<n;i++){
            for(int j=1;j<n;j++){
                if(j==1||j==9||i==j||i==10-j){
                    System.out.print("*");
                }
                else{
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
          
        // for(int i=1;i<=n;i++){
        //     for(int j=1;j<=i;j++){
        //         System.out.print("*");
        //     }
        //     for(int k=10;k>=2*i+1;k--){
        //         System.out.print(" ");
        //     }
        //     for(int j=1;j<=i;j++){
                
        //             System.out.print("*");
                
        //     }
        //     System.out.println();
        // }
        // for(int i=5;i>0;i--){
        //     for(int j=1;j<=i;j++){
        //         System.out.print("*");
        //     }
        //     for(int k=10;k>=2*i+1;k--){
        //         System.out.print(" ");
        //     }
        //     for(int j=1;j<=i;j++){
                
        //             System.out.print("*");
                
        //     }
        //     System.out.println();
        // }
    }
    
}
