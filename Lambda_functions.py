''' hay que tener en cuenta que en realidad se llaman
ANONYMOUS functions y trabajan tanto en R como en python... muy muy
utiles en ambos casos'''


'''el modelo de lambda function mas simple que hay... en el que se pasa 
lambda variables: operaciones y aquí abajo se ejemplifica''' 
# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1 * echo)
# Call echo_word: result
result = echo_word('hey', 5)
# Print result
print(result)
#---------------------------------------------------------------------------
'''este codigo deberia agregar !!! a cada palabra de la lista spells a traves
de la funcion lambda que forme, pero al imprimierlas no sucede igual,
no se porque, algo no anda bien... tengo que corregirlo'''
# Create a list of strings: spells
spells = ['protego', 'accio', 'expecto patronum', 'legilimens']
# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item +'!!!', spells)
# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)
# Print the result
print(shout_spells_list)
#---------------------------------------------------------------------------
'''Ahora si vamos con la misma funcion pero aplicando un filtro sobre una
lista o sobre un grupo de datos'''

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6, fellowship)
# Convert result to a list: result_list
result_list = list(result)
# Print result_list
print(result_list)

#-----------------------------------------------------------------------------------
# Import reduce from functools
from functools import reduce
# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)
# Print the result
print(result)
#---------------------------------------------------------------------------------



