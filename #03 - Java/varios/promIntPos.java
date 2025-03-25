/* 
Realizar un programa que calcule el promedio de notas de un grupo de alumnos. 

CONDICIONES:
1) Las notas deben variar entre 1 y 10
2) Una nota negativa no será tomada en cuenta
3) Ingresar 0 provocará el fin del ingreso
4) Debe utilizarse una función particular para el calculo del promedio (mayor expresividad y declaratividad)
5) Olvidamos momentaneamente la existencia de la función que calcula directamente el promedio de una lista
*/



import java.util.ArrayList;
import java.util.Scanner;
import java.util.List;


public class promIntPos {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingresemos las notas de los alumnos del curso. Las mismas varían entre 1 y 10.");

        List <Integer> notas = new ArrayList<>();

        System.out.println("Ingrese 0 para finalizar ingreso!");
        System.out.println("-----------------------------");
        while (true){
            System.out.print("Ingreso de la nota N°" + ((notas.size()) + 1) + ": ");
            int nota = scanner.nextInt();

            if(nota == 0){
                break;
            }else if(1 <= nota && nota <= 10){          // Interesante...
                notas.add(nota);
            }else if(nota >10){
                System.exit(0);
            }else{                  // Numero negativo --> ignorado
            }
        }

        System.out.println("El promedio de notas total fue: " + promedioDeEnteros(notas));

        scanner.close();
    }
    
    public static int promedioDeEnteros(List <Integer> lista){
        Integer sumaTotal = 0;

        for(int i = 0; i < lista.size(); i++){
            sumaTotal += lista.get(i);
        }

        int promedio = sumaTotal / lista.size();
        return promedio;

    }
}


