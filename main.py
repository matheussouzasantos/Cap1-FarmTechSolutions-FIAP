import math  # Joao - necessario para calcular area do circulo (pi)

# Matheus - Dados a serem gravados em vetores(listas)
plantios = []
culturas = []
comprimentos = []
larguras = []
raios = []
areas = []
insumos = []
dosagens = []

insumos_por_cultura = {
    "Soja": [
        "Fungicida",
        "Herbicida",
        "Inseticida",
        "Fertilizante NPK",
        "Adubo foliar",
        "Calcario",
    ],
    "Milho": [
        "Herbicida",
        "Fungicida",
        "Inseticida",
        "Fertilizante nitrogenado",
        "Fertilizante NPK",
        "Calcario",
    ],
}


def escolher_insumo(cultura, titulo):
    opcoes_insumos = insumos_por_cultura[cultura]

    print(f"\n{titulo} para {cultura}:")
    for n, insumo in enumerate(opcoes_insumos):
        print(f"{n + 1}. {insumo}")
    print("0. Digitar outro insumo")

    while True:
        try:
            opcao_insumo = int(input("Escolha uma opcao: "))
            if opcao_insumo >= 0 and opcao_insumo <= len(opcoes_insumos):
                break
            print("Opcao invalida.")
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.")

    if opcao_insumo == 0:
        while True:
            produto = input("Digite o produto/insumo: ").strip()
            if produto != "":
                return produto
            print("Produto/insumo nao pode ficar vazio.")

    return opcoes_insumos[opcao_insumo - 1]


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
        print("Opcao invalida.")
        opcao_menu = int(input("Escolha uma opcao: "))

    # Matheus - Abas do Menu
    match opcao_menu:
        case 1:
            print("\n---------- CADASTRAR PLANTIO ----------")
            nome_plantio = input("Digite o nome do plantio: ")

            print("\n1. Soja (area circular / pivo central)")
            print("2. Milho (area retangular / talhao)")
            print("\n0. Voltar ao menu principal")
            opcao_cultura = int(input("\nOpcao: "))

            # Matheus - Teste para ver se a opcao escolhida existe
            while opcao_cultura < 1 or opcao_cultura > 2:
                print("Opcao invalida.")
                opcao_cultura = int(input("Escolha uma opcao: "))

            # ----- Joao (Pessoa 2): calculo da area -----
            if opcao_cultura == 1:
                # Soja = circulo (pivo central): area = pi x raio2
                raio = float(input("Digite o raio do pivo (em metros): "))
                area = math.pi * raio ** 2
                nome_cultura = "Soja"
                # essa cultura nao usa comprimento/largura, entao grava 0
                raios.append(raio)
                comprimentos.append(0)
                larguras.append(0)
            else:
                # Milho = retangulo (talhao): area = comprimento x largura
                comprimento = float(input("Digite o comprimento do talhao (em metros): "))
                largura = float(input("Digite a largura do talhao (em metros): "))
                area = comprimento * largura
                nome_cultura = "Milho"
                # essa cultura nao usa raio, entao grava 0
                comprimentos.append(comprimento)
                larguras.append(largura)
                raios.append(0)

            # grava o resto dos dados na mesma posicao das listas
            plantios.append(nome_plantio)
            culturas.append(nome_cultura)
            areas.append(round(area, 2))

            # reserva o lugar pros insumos (Pessoa 3 preenche na opcao 5)
            insumos.append("")
            dosagens.append(0)

            print(f"\nPlantio '{nome_plantio}' ({nome_cultura}) gravado com sucesso!")
            print(f"Area calculada: {round(area, 2)} m2")
            # ----- fim da parte do Joao -----

        case 2:
            print("\n----------- CONSULTAR PLANTIOS -----------")
            # Matheus - Percorre todos os plantios e imprime no terminal
            for n, plantio in enumerate(plantios):
                print(f"{n + 1}. {plantio} | Cultura: {culturas[n]} | Area: {areas[n]}m2")
                if insumos[n] != "":
                    print(f"   Insumo: {insumos[n]} | Total necessario: {dosagens[n]} litros")

        # ----- Lucas (Pessoa 3): atualizacao de dados -----
        case 3:
            print("\n---------- ATUALIZAR PLANTIO ----------")

            if len(plantios) == 0:
                print("Nenhum plantio cadastrado para atualizar.")
            else:
                print("Escolha o plantio que deseja atualizar:")
                for n, plantio in enumerate(plantios):
                    print(f"{n + 1}. {plantio} | Cultura: {culturas[n]} | Area: {areas[n]}m2")

                print("\n0. Voltar ao menu principal")

                while True:
                    try:
                        opcao_plantio = int(input("\nEscolha uma opcao: "))
                        if opcao_plantio >= 0 and opcao_plantio <= len(plantios):
                            break
                        print("Opcao invalida.")
                    except ValueError:
                        print("Entrada invalida. Digite um numero inteiro.")

                if opcao_plantio != 0:
                    indice = opcao_plantio - 1

                    print("\nQual dado deseja atualizar?")
                    print("1. Nome do plantio")
                    print("2. Cultura e area")
                    print("3. Manejo de insumo")
                    print("0. Voltar ao menu principal")

                    while True:
                        try:
                            opcao_atualizacao = int(input("Escolha uma opcao: "))
                            if opcao_atualizacao >= 0 and opcao_atualizacao <= 3:
                                break
                            print("Opcao invalida.")
                        except ValueError:
                            print("Entrada invalida. Digite um numero inteiro.")

                    if opcao_atualizacao == 1:
                        plantios[indice] = input("Digite o novo nome do plantio: ")
                        print("Plantio atualizado com sucesso!")

                    elif opcao_atualizacao == 2:
                        print("\n1. Soja (area circular / pivo central)")
                        print("2. Milho (area retangular / talhao)")
                        print("\n0. Voltar ao menu principal")

                        while True:
                            try:
                                nova_cultura = int(input("\nOpcao: "))
                                if nova_cultura >= 0 and nova_cultura <= 2:
                                    break
                                print("Opcao invalida.")
                            except ValueError:
                                print("Entrada invalida. Digite um numero inteiro.")

                        if nova_cultura == 1:
                            while True:
                                try:
                                    raio = float(input("Digite o raio do pivo (em metros): ").replace(",", "."))
                                    if raio > 0:
                                        break
                                    print("Valor invalido. Digite um numero maior que zero.")
                                except ValueError:
                                    print("Entrada invalida. Digite um numero valido.")

                            area = math.pi * raio ** 2
                            culturas[indice] = "Soja"
                            raios[indice] = raio
                            comprimentos[indice] = 0
                            larguras[indice] = 0
                            areas[indice] = round(area, 2)
                            insumos[indice] = ""
                            dosagens[indice] = 0
                            print("Cultura e area atualizadas com sucesso!")
                            print("Manejo de insumo apagado para evitar dados inconsistentes.")

                        elif nova_cultura == 2:
                            while True:
                                try:
                                    comprimento = float(input("Digite o comprimento do talhao (em metros): ").replace(",", "."))
                                    if comprimento > 0:
                                        break
                                    print("Valor invalido. Digite um numero maior que zero.")
                                except ValueError:
                                    print("Entrada invalida. Digite um numero valido.")

                            while True:
                                try:
                                    largura = float(input("Digite a largura do talhao (em metros): ").replace(",", "."))
                                    if largura > 0:
                                        break
                                    print("Valor invalido. Digite um numero maior que zero.")
                                except ValueError:
                                    print("Entrada invalida. Digite um numero valido.")

                            area = comprimento * largura
                            culturas[indice] = "Milho"
                            comprimentos[indice] = comprimento
                            larguras[indice] = largura
                            raios[indice] = 0
                            areas[indice] = round(area, 2)
                            insumos[indice] = ""
                            dosagens[indice] = 0
                            print("Cultura e area atualizadas com sucesso!")
                            print("Manejo de insumo apagado para evitar dados inconsistentes.")
                        else:
                            print("Voltando ao menu principal...")

                    elif opcao_atualizacao == 3:
                        produto = escolher_insumo(culturas[indice], "Novo produto/insumo")

                        while True:
                            try:
                                total_litros = float(input("Novo total necessario (em litros): ").replace(",", "."))
                                if total_litros > 0:
                                    break
                                print("Valor invalido. Digite um numero maior que zero.")
                            except ValueError:
                                print("Entrada invalida. Digite um numero valido.")

                        insumos[indice] = produto
                        dosagens[indice] = round(total_litros, 2)
                        print("Manejo de insumo atualizado com sucesso!")
                    else:
                        print("Voltando ao menu principal...")

        # ----- Lucas (Pessoa 3): delecao de dados -----
        case 4:
            print("\n----------- EXCLUIR PLANTIO -----------")

            if len(plantios) == 0:
                print("Nenhum plantio cadastrado para excluir.")
            else:
                print("Escolha o plantio que deseja excluir:")
                for n, plantio in enumerate(plantios):
                    print(f"{n + 1}. {plantio} | Cultura: {culturas[n]} | Area: {areas[n]}m2")

                print("\n0. Voltar ao menu principal")

                while True:
                    try:
                        opcao_plantio = int(input("\nEscolha uma opcao: "))
                        if opcao_plantio >= 0 and opcao_plantio <= len(plantios):
                            break
                        print("Opcao invalida.")
                    except ValueError:
                        print("Entrada invalida. Digite um numero inteiro.")

                if opcao_plantio != 0:
                    indice = opcao_plantio - 1
                    nome_excluido = plantios[indice]

                    # Matheus - Remove o plantio escolhido e seus dados relacionados
                    plantios.pop(indice)
                    culturas.pop(indice)
                    comprimentos.pop(indice)
                    larguras.pop(indice)
                    raios.pop(indice)
                    areas.pop(indice)
                    insumos.pop(indice)
                    dosagens.pop(indice)

                    print(f"Plantio '{nome_excluido}' excluido com sucesso!")
                else:
                    print("Voltando ao menu principal...")

        # ----- Lucas (Pessoa 3): calculo de manejo de insumos -----
        case 5:
            print("\n----------- CALCULAR INSUMOS -----------")

            if len(plantios) == 0:
                print("Nenhum plantio cadastrado para calcular insumos.")
            else:
                print("Plantios cadastrados:")
                for n, plantio in enumerate(plantios):
                    print(f"{n + 1}. {plantio} | Cultura: {culturas[n]} | Area: {areas[n]}m2")

                print("\n0. Voltar ao menu principal")

                while True:
                    try:
                        opcao_plantio = int(input("\nEscolha uma opcao: "))
                        if opcao_plantio >= 0 and opcao_plantio <= len(plantios):
                            break
                        print("Opcao invalida.")
                    except ValueError:
                        print("Entrada invalida. Digite um numero inteiro.")

                if opcao_plantio != 0:
                    indice = opcao_plantio - 1

                    produto = escolher_insumo(culturas[indice], "Produto/insumo")

                    print("\nUnidade da quantidade aplicada por metro:")
                    print("1. mL por metro")
                    print("2. litros por metro")

                    while True:
                        try:
                            opcao_unidade = int(input("Escolha uma opcao: "))
                            if opcao_unidade == 1 or opcao_unidade == 2:
                                break
                            print("Opcao invalida.")
                        except ValueError:
                            print("Entrada invalida. Digite um numero inteiro.")

                    while True:
                        try:
                            quantidade_por_metro = float(input("Quantidade aplicada por metro: ").replace(",", "."))
                            if quantidade_por_metro > 0:
                                break
                            print("Valor invalido. Digite um numero maior que zero.")
                        except ValueError:
                            print("Entrada invalida. Digite um numero valido.")

                    while True:
                        try:
                            comprimento_rua = float(input("Comprimento da rua (em metros): ").replace(",", "."))
                            if comprimento_rua > 0:
                                break
                            print("Valor invalido. Digite um numero maior que zero.")
                        except ValueError:
                            print("Entrada invalida. Digite um numero valido.")

                    while True:
                        try:
                            quantidade_ruas = int(input("Quantidade de ruas: "))
                            if quantidade_ruas > 0:
                                break
                            print("Valor invalido. Digite um numero inteiro maior que zero.")
                        except ValueError:
                            print("Entrada invalida. Digite um numero inteiro.")

                    if opcao_unidade == 1:
                        total_ml = quantidade_por_metro * comprimento_rua * quantidade_ruas
                        total_litros = total_ml / 1000
                    else:
                        total_litros = quantidade_por_metro * comprimento_rua * quantidade_ruas
                        total_ml = total_litros * 1000

                    insumos[indice] = produto
                    dosagens[indice] = round(total_litros, 2)

                    print("\nManejo de insumo calculado com sucesso!")
                    print(f"Cultura: {culturas[indice]}")
                    print(f"Produto/insumo: {produto}")
                    print(
                        f"Calculo: {quantidade_por_metro} "
                        f"{'mL' if opcao_unidade == 1 else 'litros'}/metro x "
                        f"{comprimento_rua} metros x {quantidade_ruas} ruas"
                    )
                    print(f"Total: {round(total_ml, 2)} mL")
                    print(f"Total em litros: {round(total_litros, 2)} litros")
                else:
                    print("Voltando ao menu principal...")

        case 6:
            # Matheus - Break para sair do loop do Menu, ou seja, sair do programa
            print("\nEncerrando programa...")
            break
# Matheus - Fim menu
