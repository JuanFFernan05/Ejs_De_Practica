/* 
 Crea un programa en Java que implemente dos métodos para saludar y despedirse. El ejercicio es parecido a Función saludo y despedida, aunque el método de saludo debe tener un parámetro llamado nombre de tipo texto. 
 Luego, llama a estos métodos desde la función principal (Main) del programa.
*/

import java.util.Scanner;

public class SalYDesp {
    public static void saludar(String nombre){
        System.out.println("Hola " + nombre);
    }

    public static void despedir(){
        System.out.println("Adios!");
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese su nombre: ");
        String nombre = scanner.next();

        saludar(nombre);
        despedir();

        scanner.close();
    }


}
