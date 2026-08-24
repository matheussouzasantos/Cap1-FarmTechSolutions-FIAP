 import math  # João - necessário para calcular área do círculo (pi)

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
            nome_plantio = input("Digite o nome do plantio: ")

            print("\n1. Soja (área circular / pivô central)")
            print("2. Milho (área retangular / talhão)")
            print("\n0. Voltar ao menu principal")
            opcao_cultura = int(input("\nOpcao: "))

            # Matheus - Teste para ver se a opcao escolhida existe
            while opcao_cultura < 1 or opcao_cultura > 2:
                print("Opção inválida.")
                opcao_cultura = int(input("Escolha uma opção: "))

            # ----- João (Pessoa 2): cálculo da área -----
            if opcao_cultura == 1:
                # Soja = círculo (pivô central): área = pi x raio²
                raio = float(input("Digite o raio do pivô (em metros): "))
                area = math.pi * raio ** 2
                nome_cultura = "Soja"
                # essa cultura não usa comprimento/largura, então grava 0
                raios.append(raio)
                comprimentos.append(0)
                larguras.append(0)
            else:
                # Milho = retângulo (talhão): área = comprimento x largura
                comprimento = float(input("Digite o comprimento do talhão (em metros): "))
                largura = float(input("Digite a largura do talhão (em metros): "))
                area = comprimento * largura
                nome_cultura = "Milho"
                # essa cultura não usa raio, então grava 0
                comprimentos.append(comprimento)
                larguras.append(largura)
                raios.append(0)

            # grava o resto dos dados na mesma posição das listas
            plantios.append(nome_plantio)
            culturas.append(nome_cultura)
            areas.append(round(area, 2))

            # reserva o lugar pros insumos (Pessoa 3 preenche na opção 5)
            insumos.append("")
            dosagens.append(0)

            print(f"\nPlantio '{nome_plantio}' ({nome_cultura}) gravado com sucesso!")
            print(f"Área calculada: {round(area, 2)} m²")
            # ----- fim da parte do João -----



        case 2:
            print("\n----------- CONSULTAR PLANTIOS -----------")
            # Matheus - Percorre todos os plantios e imprime no terminal
            for n, plantio in enumerate(plantios):
                print(f"{n + 1}. {plantio} | Cultura: {culturas[n]} | Área: {areas[n]}m²")



        case 3:
            print("\n---------- ATUALIZAR PLANTIO ----------")
            print("Escolha o plantio que deseja atualizar:")
            # Matheus - Percorre todos os plantios e imprime no terminal
            for n, plantio in enumerate(plantios):
                print(f"{n + 1}. {plantio} | Cultura: {culturas[n]} | Área: {areas[n]}m²")

            print("\n0. Voltar ao menu principal")
            opcao_plantio = int(input("\nEscolha uma opção: "))

            # Matheus - Teste para ver se a opcao escolhida existe
            while opcao_plantio < 0 or opcao_plantio > len(plantios):
                print("Opção inválida.")
                opcao_plantio = int(input("Escolha uma opção: "))



        case 4:
            print("\n----------- EXCLUIR PLANTIO -----------")
            print("Escolha o plantio que deseja excluir:")
            # Matheus - Percorre todos os plantios e imprime no terminal
            for n, plantio in enumerate(plantios):
                print(f"{n + 1}. {plantio} | Cultura: {culturas[n]} | Área: {areas[n]}m²")

            print("\n0. Voltar ao menu principal")
            opcao_plantio = int(input("\nEscolha uma opção: "))

            # Matheus - Teste para ver se a opcao escolhida existe
            while opcao_plantio < 0 or opcao_plantio > len(plantios):
                print("Opção inválida.")
                opcao_plantio = int(input("Escolha uma opção: "))

            if opcao_plantio != 0:
                # Matheus - Remove o plantio escolhido e seus dados relacionados
                plantios.pop(opcao_plantio - 1)
                culturas.pop(opcao_plantio - 1)
                comprimentos.pop(opcao_plantio - 1)
                larguras.pop(opcao_plantio - 1)
                raios.pop(opcao_plantio - 1)
                areas.pop(opcao_plantio - 1)
                insumos.pop(opcao_plantio - 1)
                dosagens.pop(opcao_plantio - 1)

                print("Plantio excluído com sucesso!")
            else:
                print("Voltando ao menu principal...")



        case 5:
            print("\n----------- CALCULAR INSUMOS -----------")
            print("Plations cadastrados:")
            # Matheus - Percorre todos os plantios e imprime no terminal
            for n, plantio in enumerate(plantios):
                print(f"{n + 1}. {plantio} | Cultura: {culturas[n]} | Área: {areas[n]}m²")

            print("\n0. Voltar ao menu principal")
            opcao_plantio = int(input("\nEscolha uma opção: "))

            # Matheus - Teste para ver se a opcao escolhida existe
            while opcao_plantio < 0 or opcao_plantio > len(plantios):
                print("Opção inválida.")
                opcao_plantio = int(input("Escolha uma opção: "))

            if opcao_plantio != 0:
                # Aqui deve ser feito o Calculo de Insumos!
                print("Calculo de insumos ainda precisa ser codado!")
            else:
                print("Voltando ao menu principal...")



        case 6:
            # Matheus - Break para sair do loop do Menu, ou seja, sair do programa
            print("\nEncerrando programa...")
            break
# Matheus - Fim menu
