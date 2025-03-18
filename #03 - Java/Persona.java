public class Persona {
    String fName = "Juan Francisco", lName = "Fernández";
    Integer age = 18;

    public static void main(String[] args){
        Persona martin = new Persona();       // 1er Instancia
        martin.age = 21;    // MODIFICACIÓN DE ATRIBUTOS
        martin.fName = "Martin Enrique";
        Persona juan = new Persona();         // 2nda Instancia

        System.out.println(martin.fName + ", de " + martin.age + " años de edad, es hermano de " + juan.fName + ", de " + juan.age + " años.");
    }
    
}
