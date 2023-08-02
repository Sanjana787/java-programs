public class Prime1 {
    public static void main(String[] args) {
        int num=3,flag=0;
        for(int i=2;i*i<num;i++){
            if(num%i!=0){
                flag=1;
            }
        }
        if(flag==0){
            System.out.println("Number is prime!!");
        }
        else{
            System.out.println("Number is not prime!!");
        }
    }
}
