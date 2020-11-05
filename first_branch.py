def run():
    num_1 = int(input('Escribe un numero entero: '))
    num_2 = int(input('Escribe otro numero entero: '))

    if num_1 > num_2:
        print('El primer numero es mayor al segundo numero')
    elif num_1 < num_2:
        print('El segundo numero es  mayor al primer numero')    
    else:
        print('Los numeros son iguales')



if __name__ == "__main__":
        run()