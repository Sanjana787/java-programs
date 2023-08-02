public class Calc {
    public static void main(String[] args) {
       int a=30,b=10;
       System.out.println("--MENU--\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division");
       switch(1){
        case 1:System.out.println((a+b));  
                // break;
        case 2:System.out.println((a-b));  
                // break; 
        case 3:System.out.println((a*b));  
                // break;
        case 4:System.out.println((a/b));  
                // break;
        case 5:System.out.println((a%b));  
                // break;
            }
    }
}
