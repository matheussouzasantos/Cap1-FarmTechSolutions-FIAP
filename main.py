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
            
            # Aqui deve ser pedido e gravado os dados como: largura/comprimento ou raio (dependendo da cultura)
            # Após isso deve-se ter uma formula para calcular e gravar a área. 
            
            print(f"Plantio '{nome_plantio}' gravado com sucesso!")



        case 2:
            print("\n----------- CONSULTAR PLANTIOS -----------")
            # Matheus - Percorre todos os plantios e imprime no terminal
            for n, plantio in enumerate(plantios):
                print(f"{n + 1}. {plantio}")
                print(f"- Cultura: {culturas[n]}")
                print(f"- Área: {areas[n]}m²")
                #print(f"- Área: {areas[n]}") <- Falta cálculo de área para habilitar



        case 3:
            print("\n---------- ATUALIZAR PLANTIO ----------")
            print("Escolha o plantio que deseja atualizar:")
            # Matheus - Percorre todos os plantios e imprime no terminal
            for n, plantio in enumerate(plantios):
                print(f"{n + 1}. {plantio}")
                print(f"- Cultura: {culturas[n]}")
                print(f"- Área: {areas[n]}m²")
            opcao_plantio = int(input("Escolha uma opção: "))



        case 4:
            print("\n----------- EXCLUIR PLANTIO -----------")
            print("Escolha o plantio que deseja excluir:")
            # Matheus - Percorre todos os plantios e imprime no terminal
            for n, plantio in enumerate(plantios):
                print(f"{n + 1}. {plantio}")
                print(f"- Cultura: {culturas[n]}")
                print(f"- Área: {areas[n]}m²")
            opcao_plantio = int(input("Escolha uma opção: "))


        case 5:
            print("\n----------- CALCULAR INSUMOS -----------")



        case 6:
            # Matheus - Break para sair do loop do Menu, ou seja, sair do programa
            print("\nEncerrando programa...")
            break
# Matheus - Fim menu