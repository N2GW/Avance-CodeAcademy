"""***********  Boolean Variables  *********

#Boleanos: True o False. Se pueden crear de varias formas, pero la mas sencilla es creando una variable 
           True o False, tambien, podemos crear variables con expresiones booleanas usando operadores 
           de comparación ( == , != , >  , => etc) que nos devolveran True o False.

           
my_baby_bool = "true"
print(type(my_baby_bool))
my_baby_bool_two = True
print(type(my_baby_bool_two))

type() devuelve el tipo de dato de un objeto, por ejemplo que tipo de variable es una variable o un valor. (**A**)"""

"""*********   If Statement (Declaracion)   ********

user_name = "angela_catlady_87"

if user_name == "angela_catlady_87":
  print("Get off my computer Dave!")
  
# Aqui definimos una variable para luego utilizarla con la declaración if para luego comparar con ==."""  


"""***********  Sentencia Match.  *************

user_name = "Dave"  
match user_name:  
    case "Dave":  
        print("Get off my computer Dave!")  
    case "angela_catlady_87":  
        print("I know it is you, Dave! Go away!")   
    case "Codecademy":  
        print("Access Granted.")  
    case default:  
        print("Username not recognized.") 

# Cúando usar sentencia match en python?

 - Podemos usar sentencia match-case en alternativa a las sentencias
 if-elif-else. En caso de que una variable o expresión pueda
 tomar multiples valores, y necesitaremos realizar una acción
 diferente para cada valor posible.
- Un bloque match-case puede utilizarse para otras tareas, 
 como la coincidencia de patrones estructurales, además 
 de para sustituir a los bloques if-else. Esto nos ayuda 
 a comprobar diferentes condiciones en objetos Python como 
 listas, tuplas y cadenas.
- son más legibles que las sentencias if-elif-else. 
  Por lo tanto, en los casos en los que debamos comprobar
  muchos valores que puede tomar una expresión o variable
"""


"""***************     LIST      ***************

 # Métodos de listas

 .append():
 
  - Agrega un elemento final de la lista.
  - Ejemplo: mi_lista.append(5)

 .extend():

  - Agrega los elementos de otra lista al final de la lista actual.
  - Ejemplo: mi_lista.extend([6, 7])
 
 .insert():

  - Inserta un elemento en una posición específica.
  - Ejemplo: mi_lista.insert(1, "nuevo") (inserta nuevo en el indice 1)

 .remove():

  - Elimina la primera aparición de un valor especifico.
  - Ejemplo: mi_lista.remove(3)

 .pop():

  - Elimina y retorna el elemento en el índice especificado (o el último si no se especifica).
  - Ejemplo: elemento = mi_lista.pop() (elimina y retorna el último elemento)

 .index():

  - Retorna el índice de la primera aparición de un valor específico.
  - Ejemplo: indice = mi_lista.index(2)

 .count():

  - Retorna el número de veces que un valor aparece en la lista.
  - Ejemplo: mi_lista.reverse()

 .reverse():

  - Invierte el orden de los elementos de la lista.
  - Ejemplo: mi_lista.reverse()

 .clear():

  - Elimina todo los elementos de la lista.
  - Ejemplo: mi_lista.clear()

 .sort():

  - Ordena la lista en su lugar, lo que significa que modifica la lista original y no devuelve una lista nueva.
  - Ejemplo: mi_lista.sort() o mi_lista.sort(reverse=False)
                                             reverse: Si se establece en True, la lista se ordenará en orden descendente.
 .sorted():

  - La función sorted() devuelvee una nueva lista que contiene todos los elementos de la iterable ordenados, la iterable original no se modifica."""

"""*********************************************** Funcion len ************************************

- Se utiliza para obtener la longitud de un objeto.
- len(objeto). objeto: el objeto del cual quieres saber la longitud.

 Notas
  
  - Len() Siempre devuelve un número entero que representa la cantidad de elementos en el objeto
  - La funcion es muy útil para controlar bucles, validar entradas o simplemente para obtener informacion

 Sintaxis

 # Longitud de una cadena
cadena = "Hola, mundo"
print(len(cadena))  # Salida: 12

# Longitud de una lista
lista = [1, 2, 3, 4, 5]
print(len(lista))  # Salida: 5

# Longitud de un diccionario
diccionario = {'a': 1, 'b': 2}
print(len(diccionario))  # Salida: 2
"""
                                             
"""*************************************** Tuplas ***********************************************

# Las tuplas son una de las estructuras de datos incorporadas en Python. Al igual que las listas, las tuplas pueden contener una secuencia 
de elementos y tienen algunas ventajas clave:
 
# Las tuplas son más eficientes en memoria que las listas. Las tuplas tienen una eficiencia temporal ligeramente superior a las listas.
Esto se debe principalmente a que las tuplas son inmutables, lo que significa que no podemos modificar los elementos de una tupla después
de crearla, y no requieren un bloque de memoria adicional como las listas. 

Tuplas

En Python, las tuplas se definen con paréntesis () con valores separados por comas. Al igual que las listas, las tuplas son secuencias
y pueden contener objetos de diferentes tipos de datos.

Esta tupla tiene 4 elementos. Podemos ver que tenemos 4 elementos separados por comas:

mi_tupla = ('abc', 123, 'def', 456)

Las tuplas pueden contener un elemento siempre que éste vaya seguido de una coma:

mi_tupla = ('abc',)

Indexación y división de tuplas
Se puede acceder a los elementos de una tupla mediante su índice, es decir, su posición en la tupla. Observa la siguiente tupla:

mi_tupla = ('abc', 123, 'def', 456, 789, 'ghi')

Los índices pueden utilizarse para acceder a elementos específicos de esta tupla. Por ejemplo, si queremos acceder al primer elemento, 
podemos usar el índice 0 (¡recuerda que Python es un lenguaje de índice cero!). Escribimos el nombre de la tupla seguido de los corchetes [] 
que contienen el índice para acceder al elemento. Este código imprimiría el primer elemento, 'abc'.

print(mi_tupla[0]) # imprime abc

También podemos aplicar el corte, utilizando un rango de índices para acceder a varios elementos como en una lista. Los paréntesis deben contener
el primer índice así como el índice del final del elemento, separados por :. Este código imprimiría los elementos en las posiciones 3
y 4:

print(mi_tupla[3:5]) # imprime (456, 789)

########################## Funciones incorporadas comunes ####################################

A diferencia de las listas, las tuplas tienen un número limitado de funciones integradas, ya que son inmutables.
A continuación veremos algunas de ellas:

len()
La longitud de una tupla puede medirse utilizando la función incorporada len(). Toma la tupla como argumento para contar los elementos
de la tupla.

mi_tupla = ('abc', 123, 'def', 456, 789, 'ghi')
print(len(mi_tupla)) # imprime 6

max()
La función incorporada max() devuelve el valor máximo de la tupla. Tenga en cuenta que esta función requiere que todos los valores sean
del mismo tipo de datos. Si se utiliza con valores numéricos, la función devuelve el valor máximo. Si se utiliza con valores de cadena,
la función devuelve el valor en el índice máximo de la tupla como si estuviera ordenada alfabéticamente. La cadena más cercana a la
letra «Z» del alfabeto tendría un índice mayor.

mi_tupla = (65, 2, 88, 101, 25)
max(mi_tupla) # devuelve 101
 
mi_tupla = ('naranja', 'azul', 'rojo', 'verde')
max(mi_tupla) # devuelve «rojo»
 
mi_tupla = ('abc', 234, 567, 'def')
max(mi_tupla) # ¡lanza un error!

min()
La función integrada min() devuelve el valor mínimo de la tupla. Al igual que la función max(), la función min() requiere que todos los valores
sean del mismo tipo. Si se utiliza con valores numéricos, la función devuelve el valor mínimo. Si se utiliza con valores de cadena, 
la función devuelve el valor en el índice mínimo de la tupla como si estuviera ordenada alfabéticamente. La cadena más cercana a la letra «A» 
del alfabeto tendría un índice más bajo.

mi_tupla = (65, 2, 88, 101, 25)
min(mi_tupla) # devuelve 2
mi_tupla = ('naranja', 'azul', 'rojo', 'verde')
min(mi_tupla) # devuelve «azul
mi_tupla = ('abc', 234, 567, 'def')
min(mi_tupla) # ¡lanza un error!

.index()
El método incorporado `.index()' toma un valor como argumento para encontrar su índice en la tupla.

mi_tupla = ('abc', 234, 567, 'def')
mi_tupla.index('abc') # devuelve 0
mi_tupla.index(567) # devuelve 2

.count()
El método incorporado `.count()' toma un valor como argumento para encontrar el número de ocurrencias en la tupla.

mi_tupla = ('abc', 'abc', 2, 3, 4)
mi_tupla.count('abc') # devuelve 2
mi_tupla.count(3) # devuelve 1
"""


"""********************************************** Función Zip ****************************************************

- En python, tenemos un surtido de funciones incorporadas que nos permiten
construir nuestros programas de forma más rápida y limpa. Una de esas
funciones es zip().

- La función zip() nos permite combinar rápidamente conjuntos de datos asociados 
sin necesidad de recurrir a listas multidimensionales. Aunque zip() puede trabajar 
con muchos escenarios diferentes, vamos a explorar sólo uno.
"""