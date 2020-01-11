listaMotor = []
listaBrakes = []
listaChassis = []

# função consumíveis motor
def engine():
    motor = ["[Nº1 #Óleo motor]", "[Nº2 #Filtro de óleo]", "[Nº3 #Filtro de ar]",
             "[Nº4 #Filtro de habitáculo]", "[Nº5 #Filtro de combustível]"]

    TAMANHO = '=*' * 15
    print(TAMANHO)
    print(' ' * 7, "Motor")
    print(TAMANHO)
    print("")

    for i in motor:
        print(i)
    print("")
    print("[Nº9 #Voltar]")
    escolha = False
    while not escolha:
        cont_motor = 0
        opcao = (int(input("Escolha consumível: ")))
        if opcao == 1:
            cont_motor += 1
            listaMotor.append(motor[0])
        elif opcao == 2:
            cont_motor += 1
            listaMotor.append(motor[1])
        elif opcao == 3:
            cont_motor += 1
            listaMotor.append(motor[2])
        elif opcao == 4:
            listaMotor.append(motor[3])
        elif opcao == 5:
            listaMotor.append(motor[4])
        elif opcao == 9:
            escolha = True
            items()

# função consumíveis travagem
def brakes():
    travagem = ["[Nº1 #Calços frente]", "[Nº2 #Calços trás]", "[Nº3 #Discos trás]",
                "[Nº4 #Discos frente]", "[Nº5 #Cintas de travão]"]

    TAMANHO = '=*' * 18
    print(TAMANHO)
    print(' ' * 7, "Travagem")
    print(TAMANHO)
    print("")

    for i in travagem:
        print(i)
    print("")
    print("[Nº9 #Voltar]")
    escolha = False
    while not escolha:
        opcao = (int(input("Escolha consumível: ")))
        if opcao == 1:
            listaBrakes.append(travagem[0])
        elif opcao == 2:
            listaBrakes.append(travagem[1])
        elif opcao == 3:
            listaBrakes.append(travagem[2])
        elif opcao == 4:
            listaBrakes.append(travagem[3])
        elif opcao == 5:
            listaBrakes.append(travagem[4])
        elif opcao == 9:
            escolha = True
            items()

# função consumíveis chassis
def body():
    chassis = ["[Nº1 #Amortecedores]", "[Nº2 #Pneus]", "[Nº3 #Rolamento frente]",
               "[Nº4 #Rolamento trás]", "[Nº5 #Lâmpadas]", "[Nº6 #Escovas limpa-vidros]"]

    TAMANHO = '=*' * 15
    print(TAMANHO)
    print(' ' * 7, "Chassis")
    print(TAMANHO)
    print("")

    for i in chassis:
        print(i)
    print("")
    print("[Nº9 #Voltar]")
    escolha = False
    while not escolha:
        opcao = (int(input("Escolha consumível: ")))
        if opcao == 1:
            listaChassis.append(chassis[0])
        elif opcao == 2:
            listaChassis.append(chassis[1])
        elif opcao == 3:
            listaChassis.append(chassis[2])
        elif opcao == 4:
            listaChassis.append(chassis[3])
        elif opcao == 5:
            listaChassis.append(chassis[4])
        elif opcao == 6:
            listaChassis.append(chassis[5])
        elif opcao == 9:
            escolha = True
            items()

# função dados viatura + grava txt
def dados_viatura ():
    print("Insira dados da viatura: ")
    print('-' * 50)
    marca = (str(input("Marca: ")))
    modelo = (str(input("Modelo: ")))
    cilindrada = (str(input("Cilindrada: ")))
    data_matricula = (str(input("Data matrícula: ")))
    print('-' * 50)
    print('-' * 50)

    TAMANHO = '-' * 50
    import os.path
    directory = 'C:\Python_output'
    filename = "Registo.txt"
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    file = open(file_path, "a+")
    data = (str(input("Insira a data: ")))
    file.write(f"{'*' * 50}\n")
    file.write(f"Registo de Manutenção do dia: {data}\n")
    file.write(f"{TAMANHO}\n")
    line1 = marca
    line2 = modelo
    line3 = cilindrada
    line4 = data_matricula
    file.write(f"Marca: {line1}\nModelo: {line2}\nCilindrada: {line3}\nData matrícula: {line4}\n")
    file.write(f"{TAMANHO}\n")

# função consumíveis total/geral
def items():
    lista = []
    TAMANHO = '=*' * 25
    print(TAMANHO)
    print(' ' * 7, "Registo de manutenção automóvel")
    print(TAMANHO)
    print("")
    print("")

    lista = ["[Nº1 #Motor]", "[Nº2 #Travagem]", "[Nº3 #Chassis]"]

    for i in lista:
        print(i)
    print("")
    print("[Nº9 #Sair]")
    print("[Nº0 #Novo Registo]")
    opcao = (int(input("Selecione uma categoria: ")))
    print("")
    if opcao == 1:
        engine()
    elif opcao == 2:
        brakes()
    elif opcao == 3:
        body()
    elif opcao == 0:
        resultados()
        dados_viatura()
        items()
    elif opcao == 9:
        resultados()
        print("Registo efetuado com sucesso."
              "\nConsulte 'Registo.txt', obrigado.")
        print("=" * 50)
        print("")

# função notas adicionais
def notas():
    TAMANHO = '-' * 50
    import os.path
    directory = 'C:\Python_output'
    filename = "Registo.txt"
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    file = open(file_path, "a+")

    # adiciona notas do utilizador e grava txt
    notas = (str(input("Deseja adicionar alguma nota? ")))
    file.write(f"Notas: {notas}\n")
    file.write(f"{TAMANHO}\n")

# função imprime resultados na tela e grava txt
def resultados():
    print("\n")
    print("Consumíveis do motor usados: ")
    TAMANHO = '-' * 50
    import os.path
    directory = 'C:\Python_output'
    filename = "Registo.txt"
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    file = open(file_path, "a+")
    file.write("Consumíveis do motor usados: \n")
    for i in listaMotor:
        print(i)
        file.write(f"{i}\n")
    file.write(f"{TAMANHO}\n")
    print(f"{TAMANHO}")

    print("Consumíveis de travagem usados: ")
    file.write("Consumíveis de travagem usados: \n")
    for i in listaBrakes:
        print(i)
        file.write(f"{i}\n")
    file.write(f"{TAMANHO}\n")
    print(f"{TAMANHO}")

    print("Consumíveis chassis usados: ")
    file.write("Consumíveis chassis usados: \n")
    for i in listaChassis:
        print(i)
        file.write(f"{i}\n")
    file.write(f"{TAMANHO}\n")
    print(f"{TAMANHO}")

# código principal abaixo
def main():
    dados_viatura()
    items()
    notas()
    input('Press ENTER to exit')

if __name__ == '__main__':
    main()