def run():
    ext_counter = 0
    int_counter = 0
    frutas = ['manzana','pera','mango','platano']
    estudiantes = {
        'Mexico' : 10,
        'colombia' : 15,
        'Puerto Rico' : 4,
    }


    while ext_counter <= 3:
        while int_counter <= 3:
            print(ext_counter,int_counter)
            int_counter += 1
        ext_counter += 1
        int_counter = 0
    
    
    input('Presiona enter para frutas') 

    for fruta in frutas:
        print(fruta)
    

    input('Presiona enter para looper')

    looper = iter(frutas)
    next(looper)
    input('Presiona enter')
    next(looper)
    input('Presiona enter')
    next(looper)
    input('Presiona enter')
    next(looper)
    input('Presiona enter')


    input('Presiona enter pais 1')

    for pais in estudiantes:
        print(pais)


    input('Presiona enter pais 2')

    for pais in estudiantes.keys():
        print(pais)
    

    input('Presiona enter estudiantes 1')

    for num_estudiantes in estudiantes.values():
        print(num_estudiantes)


    input('Presiona enter juntos')

    for pais,num_estudiantes in estudiantes.items():
        print(pais,num_estudiantes)




if __name__ == "__main__":
    run()