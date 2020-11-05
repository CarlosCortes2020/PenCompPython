"""
Docscreen

¿Que hace?
Muestra la diferencia entre los alcances de los diferentes tipos de variables

¿Que significan los parametros?
param un_arg entero que circula entre las funciones

¿Que regresa la funcion?

Regresa un valor calculado en el interior de funciones
a diferentes niveles

"""
def func1(un_arg,una_func):
    def func2(otro_arg):
        return otro_arg *2
    
    valor = func2(un_arg)
    return una_func(valor)

def cualquier_func(cualquier_arg):
    return cualquier_arg + 5

def run():
    
    un_arg = 1
    print(func1(un_arg,cualquier_func))


if __name__ == "__main__":
    run()