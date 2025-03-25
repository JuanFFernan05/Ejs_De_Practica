import java.util.Scanner;

public class Vocales {
 
    public static boolean tieneVocal(String string){
        return string.matches(".*[aeiouAEIOU].*");
    }

    public static void main(String[] args){
         Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese su palabra a analizar: ");
        String palabra = scanner.next();

        if(tieneVocal(palabra)){
            System.out.println(palabra + " posee vocales");
        }else{
            System.out.println(palabra + " no posee vocales.");
        }

        scanner.close();
    }
    
}
