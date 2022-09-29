library(tidyverse)
library(dslabs)
data(murders)

1. Carguen el set de datos co2 que viene incluido en la base de R. Recuerden para cargar un set de datos que viene
prediseñado dentro de un paquete o en la base de R la orden es data(nombre del database).

2. Examine el set de datos... qué orden es más adecuada y por qué,
justifiquen su respuesta al final de esta pregunta?
A. head(co2)
B. View(co2)
C. print(co2)
D. str(co2)

3. Qué comando me ayuda a conocer un reporte de mi dataframe... tipo de variables,
tamaño del dataframe, tipo de columnas, entre otros y por qué,
justifiquen su respuesta al final de esta pregunta?
A. str(co2)
B. class(co2)
C. length(co2)
D. squeeze(co2)

2. Si rank(x) le da el rango de las entradas de x de menor a mayor, rank(-x)
le da los rangos de mayor a menor. Usen la función mutate para añadir una columna
rank que contiene el rango de la tasa de asesinatos de mayor a menor.
Asegúrense de redefinir murders para poder seguir usando esta variable.

3. Con dplyr, podemos usar select para mostrar solo ciertas columnas.
Por ejemplo, con este código solo mostraríamos los estados y los tamaños de población:

---> murders %>%
   select(state, population)%>%
   head()

Utilicen select para mostrar los nombres de los estados y las abreviaturas en murders.
No redefinan murders, solo muestren los resultados y guarden estas columnas en una variable
llamada abreviaturas.

4. en el ejercicio 2 crearon una variable llamada rank en la que asignaron el rango de muestres
organizadas de mayor a menor, extráigan esta variable del dataset total y agréguenla a la variable
abreviaturas.

Qué pasó?

A. Todo perfecto, ya está hecho.
B. No se puede, los dataframes son de tamaños diferentes.
C. Los dataframes son de diferente tamaño, pero pudimos lograrlo.
D. A y B son correctas.

