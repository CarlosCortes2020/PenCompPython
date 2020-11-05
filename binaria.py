#Algoritmo de nombre busqueda binaria
def run():
    target = int(input('Escoge un numero: '))
    ipso = 0.01
    low = 0.0
    high = max(1.0,target)
    answer = (high + low) / 2

    while abs(answer**2 - target) >= ipso:
        if answer**2 < target:
            low = answer
        else:
            high = answer
        answer = (high + low) / 2
    print(f'La raiz cuadrada de {target} es {answer}')



if __name__ == "__main__":
    run()