listaMotor = []
listaBrakes = []
listaChassis = []

contador = []
file=open("teste.txt", "w")
# função consumíveis motor
def engine():
    motor = ["Nº1 #Óleo motor", "Nº2 #Filtro de óleo", "Nº3 #Filtro de ar",
             "Nº4 #Filtro de habitáculo", "Nº5 #Filtro de combustível"]

    TAMANHO = '=*' * 15
    print(TAMANHO)
    print(' ' * 7, "\33[31mMotor\33[m")
    print(TAMANHO)
    print("")

    for i in motor:
        print(i)
    print("")
    print("Nº9 #Voltar")
    escolha = False
    while not escolha:
        cont_motor = 0
        opcao = (int(input("Selecione uma opção: ")))
        contador.append(cont_motor)
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
    travagem = ["Nº1 #Calços frente", "Nº2 #Calços trás", "Nº3 #Discos trás",
                "Nº4 #Discos frente", "Nº5 #Cintas de travão", "Nº9 #Voltar"]

    TAMANHO = '=*' * 18
    print(TAMANHO)
    print(' ' * 7, "\33[31mTravagem\33[m")
    print(TAMANHO)
    print("")

    for i in travagem:
        print(i)
    print("")
    print("Nº9 #Voltar")
    escolha = False
    while not escolha:
        opcao = (int(input("Selecione uma opção: ")))
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
    chassis = ["Nº1 #Amortecedores", "Nº2 #Pneus", "Nº3 #Lâmpadas", "Nº4 #Escovas limpa-vidros", "Nº9 #Voltar"]

    TAMANHO = '=*' * 15
    print(TAMANHO)
    print(' ' * 7, "\33[31mChassis\33[m")
    print(TAMANHO)
    print("")

    for i in chassis:
        print(i)
    print("")
    print("Nº9 #Voltar")
    escolha = False
    while not escolha:
        opcao = (int(input("Selecione uma opção: ")))
        if opcao == 1:
            listaChassis.append(chassis[0])
        elif opcao == 2:
            listaChassis.append(chassis[1])
        elif opcao == 3:
            listaChassis.append(chassis[2])
        elif opcao == 4:
            listaChassis.append(chassis[3])
        elif opcao == 9:
            escolha = True
            items()


# função consumíveis total/geral
def items():
    lista = []
    TAMANHO = '=*' * 25
    print(TAMANHO)
    print(' ' * 7, "\33[31mRegisto de manutenção automóvel\33[m")
    print(TAMANHO)
    print("")
    lista = ["Nº1 #Motor", "Nº2 #Travagem", "Nº3 #Chassis"]

    for i in lista:
        print(i)
    print("")
    print("Nº9 #Sair")
    print("")
    opcao = (int(input("Selecione uma opção: ")))
    print("Opção ", opcao, " selecionada.")
    print("")
    if opcao == 1:
        engine()
    elif opcao == 2:
        brakes()
    elif opcao == 3:
        body()
    elif opcao == 9:
        print("\33[4mRegisto efetuado com sucesso, obrigado.\33[m")
        print("=" * 50)
        print("")

# código principal abaixo
items()
file = open("teste.txt", "w")
file.write(items())
print("Consumíveis do motor foram usados: ", )
for i in listaMotor:
    print(i)
print('-' * 50)
print("Consumíveis de travagem foram usados: ", )
for i in listaBrakes:
    print(i)
print('-' * 50)
print("Consumíveis chassis foi usado: ", )
for i in listaChassis:
    print(i)
print('-' * 50)

input('Press ENTER to exit')
file.close()