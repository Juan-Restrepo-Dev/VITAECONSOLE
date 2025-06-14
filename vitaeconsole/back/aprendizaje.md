# aprendizaje adquirido para realizar este proyecto

## Importaciones de ficheros del proyecto y archivos externos python

## uso de los parámetros args y kwargs en python.
En Python, *args y **kwargs se utilizan para pasar un número variable de argumentos a una función. *args recibe argumentos posicionales, mientras que **kwargs recibe argumentos con nombre (o argumentos de palabra clave). Esto es útil cuando la función debe ser flexible en el número de argumentos que puede manejar. 
Detalles:
*args (argumentos posicionales):
Permite pasar un número variable de argumentos posicionales a una función.
Dentro de la función, args se convierte en una tupla que contiene todos los argumentos pasados a través de *args.
Ejemplo: 
Python

    def mi_funcion(*args):
        print(type(args))  # Imprime: <class 'tuple'>
        for argumento in args:
            print(argumento)

    mi_funcion(1, 2, "hola", 3.14)  # Imprimirá: 1, 2, hola, 3.14
`: kwargs` (argumentos con nombre):**
Permite pasar argumentos con nombre a una función. 
Dentro de la función, kwargs se convierte en un diccionario que contiene los argumentos con nombre y sus valores. 
Ejemplo:
Python

    def mi_funcion(**kwargs):
        print(type(kwargs))  # Imprime: <class 'dict'>
        for clave, valor in kwargs.items():
            print(f"{clave}: {valor}")

    mi_funcion(nombre="Juan", edad=30, ciudad="Medellín")  # Imprimirá: nombre: Juan, edad: 30, ciudad: Medellín
Uso en la definición de funciones:
*args y **kwargs se colocan en la definición de la función, generalmente al final de la lista de parámetros. 
Ejemplo:
Python

    def mi_funcion(argumento_obligatorio, *args, **kwargs):
        print(argumento_obligatorio)
        print(args)
        print(kwargs)

    mi_funcion("Argumento obligatorio", 1, 2, nombre="Juan", edad=30)  # Imprimirá: Argumento obligatorio, (1, 2), {'nombre': 'Juan', 'edad': 30}
Orden de parámetros:
Los argumentos regulares (obligatorios) deben estar antes de *args y *kwargs. 
*args debe estar antes de **kwargs. 
En resumen:
*args y **kwargs facilitan la creación de funciones flexibles que pueden manejar un número variable de argumentos, ya sean posicionales o con nombre. 
## clase en python

## Uso de with en python

## Uso de yield en python

## uso de decoradores python

#### Decoradores
Antes de entrar de lleno con el tema de decoradores es importante mencionar que en Python las funciones son ciudadanos de primera clase, eso quiere decir que una función puede ser asignada a una variable, puede ser utilizada como argumento para otra función, o inclusive puede ser retornada. Veamos un ejemplo.

```{python}
def saludar(): 
    print('Hola soy una función') 

def super_funcion(funcion): 
    funcion() 

funcion = saludar  # Asignamos la función a una variable!

super_funcion(funcion)      
```

Listo, una vez con esto en cuenta ya podemos pasar el tema de decoradores. Si nunca oíste hablar de los decoradores, no te preocupes, aquí te lo explicamos. Verás, un decorador no es más que una función la cual toma como input una función y asu vez retorna otra función. Puede sonar algo confuso ¿no? lo que nos debe quedar claro es que al momento de implementar un decorador estaremos trabajando, con por lo menos, 3 funciones. El input, el output y la función principal. Para que nos quede más en claro a mi me gusta nombrar a las funciones como: a, b y c.

Donde a recibe como parámetro b para dar como salida a c. Esta es una pequeña "formula" la cual me gusta mucho mencionar. 💻

a(b) -> c

Veamos un ejemplo de como crear un decorador en Python.

def funcion_a(funcion_b):
    def funcion_c():
        print('Antes de la ejecución de la función a decorar')
        funcion_b()
        print('Después de la ejecución de la función a decorar')

    return funcion_c
Ya tenemos el decorador creado, ahora lo que nos hace falta es decorar una función. Al nosotros utilizar la palabra decorar estamos indicando que queremos modificar el comportamiento de una función ya existente, pero sin tener que modificar su código. Esto es muy útil, principalmente, cuando queremos extender nuevas funcionalidades a dicha función. De allí el nombre decorar.

Si me permiten, una buena analogía sería ver este tema como un pastel, donde, en ocasiones, la base del pastel (el pan) no es suficiente para una fiesta y debemos añadir elementos extras, quizás glaseado, velas, aderezos etc ... de esta forma el pastel se verá mucho mejor y lo más importante sabrá mucho mejor. 🎂

En la analogía la base del pastel no será más que nuestra función a decorar y los elementos extras los decoradores.

Para decorar una función basta con colocar, en su parte superior de dicha función, el decorador con el prefijo @.

@funcion_a
def saludar():
    print('Hola mundo!!')
Ahora, ¿Qué pasa si nuestra función a decorar debe recibir argumentos y a su vez debe retornar algún valor? en estos casos haremos uso de los parámetros args y kwargs.

def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        print('Antes de la ejecución de la función a decorar')
        result = funcion_b(*args, **kwargs)
        print('Después de la ejecución de la función a decorar')    

        return result

    return funcion_c

@funcion_a
def suma(a, b):
    return a + b
La sintaxis puede llegar a hacer algo compleja, pero en terminos simples podemos traducirlo a :

>>> decorador = funcion_a(suma)
>>> decorador(10, 20)  

Antes de la ejecución de la función a decorar
Después de la ejecución de la función a decorar
30
Al utilizar los parámetros args y kwargs seremos capaces de reutilizar el decorador, haciendolo aún más flexible de lo que ya es.

Algo que me gustaría mencionar, es que por convención, no es una regla, la función anidada del decorador tendrá por nombre: wrapper, de igual forma, el nombre del decorador debe ser muy descriptivo. En términos simples, el decorador pudiera quedar de la siguiente manera.

def my_custome_decorator(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
Este ejemplo funciona, pero, trabajamos con un ejemplo, un poco más real. Calculemos cuánto le toma a una función completar su ejecución.

def measure_time(function):
    def wrapper(*args, **kwargs):
        import time

        start = time.time()
        result = function(*args, **kwargs)
        total = time.time() - start
        print(total, 'seconds' )
        return result

    return wrapper


@measure_time
def suma(a, b):
    import time
    time.sleep(1)
    return a + b

print(suma(10, 20))
Perfecto, ya sabemos crear e implementar decoradores, sin embargo aún podemos complicar las cosas un poco más. Como mencionamos anteriormente los decoradores no son más que funciones que reciben como argumento otras funciones, en ese caso, ¿Es posible pasar argumentos extras a los decoradores? 🧐La respuesta es sí. 😉

def my_decorator_name(name):
    def my_custome_decorator(function):
        def wrapper(*args, **kwargs):

            print('Name:', name)
            return function(*args, **kwargs)

        return wrapper

    return my_custome_decorator

@my_decorator_name('CodigoFácilito')
def suma(a, b):
    return a + b
En este caso tuvimos que agregar una cuarta función, la cual recibiría los parámetros necesarios. Aquí sin duda las cosas ya se complican más, ya que ahora estamos trabajando con otro tema, el tema de los closures, tema el cual sin duda explicaremos en otra ocasión.

Ya para finalizar, algo que debemos tener muy en cuenta es que los decoradores no están limitados únicamente y exclusivamente a funciones o métodos, para nada, de igual forma podremos decorar clases, sí, leíste bien, clases. Si te interesa conocer más acerca del tema te comparto un vídeo en donde te lo explicamos más en detalle .🐍

#### FUENTE: https://codigofacilito.com/articulos/decoradores-python

## uso de la libreria dataclasses como decorador

## uso de la libreria json