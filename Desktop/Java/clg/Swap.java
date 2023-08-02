 class Swap {
    public static void main(String[] args) {
        int a=10,b=20;
        System.out.println("values before swapping are:"+a+"\n"+b);
        a=a+b;
        b=a-b;
        a=a-b;
        System.out.print("Swapped values are :"+a+"\n"+b);
    }
}
