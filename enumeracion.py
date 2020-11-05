#Algoritmo de enumeracion exhaustiva para calcular raiz 
#cuadrada d eun numero

def run():
    target = int(input('Choose an integer number: '))
    answer = 0

    while answer **2 < target:
        answer += 1

    if answer**2 == target:
        print(f'Square root of {target} is {answer}')
    else:
        print(f'{target} has not square root' )




if __name__ == "__main__":
    run()