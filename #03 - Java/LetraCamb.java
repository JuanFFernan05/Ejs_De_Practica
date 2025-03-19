/*
 Crea un programa en Java que implemente una función llamada cambiarLetra() con el propósito de modificar un carácter en un texto. 
 La función debe recibir como parámetros el texto, una posición (basada en 0) y una letra, todos solicitados al usuario. El programa debe validar la posición para asegurarse de que esté dentro del rango del texto y luego mostrar el nuevo texto resultante en pantalla.
 */

 import java.util.Scanner;


public class LetraCamb{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese un string a modificar: ");
        String string = scanner.nextLine();
        System.out.print("Ingrese el índice a modificar del string: ");
        int posicion = scanner.nextInt();
        System.out.print("Ingrese la letra a agregar: ");
        char letra = (scanner.next()).charAt(0);

        System.out.println("Palabra original: " + string);
        System.out.println("Palabra modificada: " + cambiarLetra(string, posicion, letra));

        scanner.close();
    }

    public static String cambiarLetra(String palabra, int posicion, char letra){
        if(posicion < palabra.length() && posicion >= 0){
        StringBuilder sb = new StringBuilder(palabra);          // Util para modificar cadenas!!
        sb.setCharAt(posicion, letra);
        return sb.toString();
        }else{
            throw new IllegalArgumentException("Posición fuera de rango");
        }
    }
}