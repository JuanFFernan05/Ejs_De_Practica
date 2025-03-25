import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class analisisDeLista {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
    
        List<Integer> lista = new ArrayList<>();

        while (true){
            System.out.print("Ingrese el indice " + lista.size() + " de la lista: ");
            int valor = scanner.nextInt();
            lista.add(valor);

            System.out.print("¿Desea continuar ingresando valores? 1: Si - 0: No. : ");
            int decision = scanner.nextInt();

            if(decision == 1){
            }else if(decision == 0){
                break;
            }else{
                System.out.println("ERROR. Fin de programa!");
                System.exit(0);    // Fin del programa
            }

        }
        if(!lista.isEmpty()){
        System.out.println("Su lista es: " + lista);
        System.out.println("El mayor valor de su lista es: " + mayorValorDeLista(lista));
        scanner.close();
        }else{
            System.out.println("Valores no ingresados!");
        }
    }
    
        public static int mayorValorDeLista(List<Integer> lista){

            int maximo = lista.get(0);

            for(int i = 0; i < lista.size(); i++){
                int numero = lista.get(i);

                if(numero > maximo){
                    maximo = numero;
                }
            }

            return maximo;
        }
    }
