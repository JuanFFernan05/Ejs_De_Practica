public class Auto{
    int antiguedad;         // En años, del auto
    String modelo;

    public Auto(int antiguedad, String modelo) {        // CONSTRUCTOR
        this.antiguedad = antiguedad;
        this.modelo = modelo;
    }

    public void velMaxima(){
        if(antiguedad > 10){
            System.out.println("La velocidad maxima de este modelo " + modelo + " es 120 km/h");
        }else{
            System.out.println("La velocidad maxima de este modelo " + modelo + " es 200 km/h");
        }
    }

    public void pocaGasolina(){
        System.out.println("Poca gasolina en tanque!!!!!");
    }

    public static void main(String[] args){
        Auto fitito = new Auto(12, "Fiat");
        fitito.velMaxima();

        
    }


}