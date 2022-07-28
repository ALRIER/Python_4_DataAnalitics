# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')
# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)
# Add poland to europe
europe['poland'] = 'warsaw'
# Print europe
print(europe)
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }
# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

print(europe)

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Print out the capital of France
europe['france']
# Create sub-dictionary data
data = {'capital':'rome', 'population':59.83 }
# Add data to europe under key 'italy'
europe['italy']=data
print (europe)

#lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

import pandas as pd
# Create dictionary my_dict with three key:value pairs: my_dict
my_dict={'country':names,'drives_right':dr,'cars_per_cap':cpc}
# Build a DataFrame cars from my_dict: cars
cars=pd.DataFrame(my_dict)
print (cars)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])

'''loc and iloc (1)
With loc and iloc you can do practically any data selection operation on DataFrames you can think of. loc is label-based, which means that you have to specify rows and columns based on their row and column labels. iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.

Try out the following commands in the IPython Shell to experiment with loc and iloc to select observations. Each pair of commands here gives the same result.

cars.loc['RU']
cars.iloc[4]

cars.loc[['RU']]
cars.iloc[[4]]

cars.loc[['RU', 'AUS']]
cars.iloc[[4, 1]]
As before, code is included that imports the cars data as a Pandas DataFrame.'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])

'''loc and iloc (2)
loc and iloc also allow u2 select both rows and columns from a DataFrame.'''
# Print out drives_right value of Morocco
print(cars.loc['MOR'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])

#generando iteraciones para ciclos for y loops... 

''' si lo que uno quiere es hacer iteraciones dentro de varios elementos de un
ciclo entonces uno puede crear un ciclo, denominar variables x y y y hacer que
el ciclo recorra los elementos dentro del conjunto de datos. 

en el caso de python uno puede crear iteraciones para arrelos y diccionarios
que tienen llaves keys y elementos conformados dentro... asi'''

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
''' este ciclo agarra cada elemento del diccionario europa, pero como yo 
definí un elemento X y uno Y en el loop, entonces el algoritmo recorre cada
elemento del diccionario tomando como referencia la llave de acceso al
al diccionario que en este caso sera una capital'''
for x,y in europe.items():
    print("the capital of"+str(x)+ "is " +str(y))

'''ahora iterando sobre matrices 2D'''
import numpy as np
# For loop over np_height
for X in np_height:
    print(str(X) + " inches")

# For loop over np_baseball
for X in np.nditer(np_baseball):
    print(X)
    
'''iterrows
en las diapositivas de loops'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for labs, row in cars.iterrows():
    print(labs)
    print(row)

'''   cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JPN           588          Japan         False
IN             18          India         False
RU            200         Russia          True

esta es la matriz de cars.csv y como es un dataframe hay que llamar 
el loop diferente...'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))
'''en este caso yo quería que se imprimieran dos valores
por un lado la etiqueta lab y por el otro el valor de la
columna y por eso llamé lab + str(row) de la columna 
llamara cars_per_cap'''


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab,"COUNTRY"] = row["country"].upper()
'''Aquí lo que hago es agarrar cada valor de la columna
country, lo paso a mayusculas y luego lo imprimo nuevamente 
en una nueva columna llamada "COUNTRY"'''

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)
'''esta línea hace lo mismo pero en otro orden'''

'''
Roll the dice
In the previous exercise, you used rand(), that generates a random float
between 0 and 1.

As Hugo explained in the video you can just as well use randint(),
also a function of the random package, to generate integers randomly.
The following call generates the integer 4, 5, 6 or 7 randomly.
8 is not included.

import numpy as np
np.random.randint(4, 8)
NumPy has already been imported as np and a seed has been set.
Can you roll some dice?'''

# Import numpy and set seed
import numpy as np
np.random.seed(123)
# Use randint() to simulate a dice
print(np.random.randint(1,7))
# Use randint() again
print(np.random.randint(1,7))

