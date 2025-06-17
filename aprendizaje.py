print("*decoradores")
print("-"*50)

def funcion_a(funcion_b):
    def funcion_c():
        print('Antes de la ejecución de la función a decorar')
        funcion_b()
        print('Después de la ejecución de la función a decorar')

    return funcion_c
@funcion_a
def saludar():
    print('Hola mundo!!')

saludar()

print("-"*50)


print("*decoradores usando args y Kargs")
print("-"*50)
def funcion_a2(funcion_b2):
    def funcion_c2(*args, **kwargs):
        print('Antes de la ejecución de la función a decorar')
        result = funcion_b2(*args, **kwargs)
        print('Después de la ejecución de la función a decorar')    

        return result

    return funcion_c2

@funcion_a2
def suma(a, b):
    return a + b

print(suma(2,4))

print("-"*50)