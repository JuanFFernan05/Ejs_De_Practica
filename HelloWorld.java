import java.util.List;
import java.util.ArrayList;

public class HelloWorld {
    
    public static void main(String[] args) {       
       System.out.println("Hello World!"); 

       List myList = new ArrayList(); 
       myList.add("Hola");
       myList.add(3);

       for(int i = 0; i < myList.size(); i++){      // Esto es un simple for
            System.out.println(myList.get(i));
       }
       };

       /*
        COMENTARIO 
            MULTILÍNEA 
        */



    }

    
