import java.util.Scanner;


public class Fibonacci {
    
    public static int fibonacci (int n){
        if(n <= 1){
            return n;
        }else{
            int a = 0, b = 1, c;
            for (int i = 2; i <= n; i++) {
                c = a + b;
                a = b;
                b = c;
            }
            return b;
        }
        
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Iteraciones de Fibonacci: ");
        int numero = scanner.nextInt();

        System.out.println("Perfecto, aplicaremos FIBONACCI--" + numero + "--");
        System.out.println("El término " + numero + " de Fibonacci es: " + fibonacci(numero));

        scanner.close();
    }
}

