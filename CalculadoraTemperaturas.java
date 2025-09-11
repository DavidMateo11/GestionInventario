public class CalculadoraTemperaturas  {

    public static void main(String[] args) {
        // Datos de prueba: una matriz 2D con temperaturas de varias ciudades y semanas
        double[][] datosTemperaturas = {
            {25.5, 26.0, 24.8, 27.1}, // Ciudad 1
            {15.0, 14.5, 16.2, 15.8}, // Ciudad 2
            {30.1, 29.5, 31.0, 30.5}  // Ciudad 3
        };

        // Llamamos a la función para calcular los promedios
        double[] promedios = calcularPromedioTemperaturas(datosTemperaturas);

        // Imprimimos los resultados en la consola
        System.out.println("Promedios de temperatura por ciudad:");
        for (int i = 0; i < promedios.length; i++) {
            System.out.println("Ciudad " + (i + 1) + ": " + promedios[i] + "°C");
        }
    }

    /**
     * Calcula la temperatura promedio para cada ciudad a partir de una matriz de temperaturas.
     *
     * @param temperaturas Una matriz 2D donde cada fila es una ciudad y cada columna es una semana.
     * @return Un array que contiene el promedio de temperaturas para cada ciudad.
     */
    public static double[] calcularPromedioTemperaturas(double[][] temperaturas) {
        int numCiudades = temperaturas.length;
        double[] promedios = new double[numCiudades];

        for (int i = 0; i < numCiudades; i++) {
            double suma = 0.0;
            for (int j = 0; j < temperaturas[i].length; j++) {
                suma += temperaturas[i][j];
            }
            promedios[i] = suma / temperaturas[i].length;
        }

        return promedios;
    }
}
    
