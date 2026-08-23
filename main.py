# Matheus - Dados a serem gravados em vetores(listas)
plantios = []
culturas = []
comprimentos = []
larguras = []
raios = []
areas = []
insumos = []
dosagens = []

# Matheus - Menu de escolhas
while True:
    print("\n---------- FARMTECH SOLUTIONS ----------")
    print("1. Cadastrar plantio")
    print("2. Consultar plantios")
    print("3. Atualizar plantio")
    print("4. Excluir plantio")
    print("5. Calcular manejo de insumos")
    print("6. Sair")

    opcao_menu = int(input("Escolha uma opcao: "))

    # Matheus - Teste para ver se a opcao escolhida existe
    while opcao_menu < 1 or opcao_menu > 6:
        print("Opção inválida.")
        opcao_menu = int(input("Escolha uma opção: "))

    # Matheus - Abas do Menu
    match opcao_menu:
        case 1:
            print("\n---------- CADASTRAR PLANTIO ----------")
            nome_plantio = input("Nome do plantio: ")

            print("\n1. Soja (área circular / pivô central)")
            print("2. Milho (área retangular / talhão)")
            opcao_cultura = int(input("Opcao: "))

            # Matheus - Teste para ver se a opcao escolhida existe
            while opcao_cultura < 1 or opcao_cultura > 2:
                print("Opção inválida.")
                opcao_cultura = int(input("Escolha uma opção: "))
            
            # Matheus - Gravando nos vetores
            if opcao_cultura == 1:
                comprimento_terreno = float(input("Comprimento do terreno (m): "))
                largura_terreno = float(input("Largura do terreno (m): "))
                culturas.append("Soja")
                comprimentos.append(comprimento_terreno)
                larguras.append(largura_terreno)
                raios.append(None)
            else:
                raio_terreno = float(input("Raio do terreno (m): "))
                culturas.append("Milho")
                raios.append(raio_terreno)
                comprimentos.append(None)
                larguras.append(None)
            plantios.append(nome_plantio)

            print(f"Plantio '{nome_plantio}' gravado com sucesso!")
        case 2:
            print("\n----------- CONSULTAR PLANTIOS -----------")
            # Matheus - Percorre todos os plantios e imprime no terminal
            for n, plantio in enumerate(plantios):
                print(f"{n + 1}. {plantio}")
                print(f"- Cultura: {culturas[n]}")
                #print(f"- Área: {areas[n]}") <- Falta cálculo de área para habilitar
        case 3:
            print("\n---------- ATUALIZAR PLANTIO ----------")
        case 4:
            print("\n----------- EXCLUIR PLANTIO -----------")
        case 5:
            print("\n----------- CALCULAR INSUMOS -----------")
        case 6:
            # Matheus - Break para sair do loop do Menu, ou seja, sair do programa
            print("\nEncerrando programa...")
            break
# Matheus - Fim menu