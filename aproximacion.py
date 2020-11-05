#Algoritmo de aproximación para encontrar la raiz cuadrada 
#de un número.

def run():
    target = int(input('Select a number: '))
    ipso = 0.0001
    step = ipso**2
    answer = 0.0

    while abs(answer**2 - target) >= ipso and answer <= target:
        answer += step
    if abs(answer**2 - target) >= ipso:
        print(f'No se encontró la raiz cuadrada de {target}')
    else:
        print(f'La raiz cuadrada de {target} es {answer}')


if __name__ == "__main__":
    run()