def run():
    name = input('Por favor, escribe tu nombre: ')
    name_chain = 'Hola, buen día, ' + name + ', la longitud de la cadena es:'
    out_chain = len(name_chain)  
    print(name_chain, out_chain)
    

if __name__ == "__main__":
    run()
