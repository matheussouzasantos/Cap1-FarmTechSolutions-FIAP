# 🌱 FarmTech Solutions

Projeto desenvolvido para a atividade avaliativa do curso de **Inteligência Artificial da FIAP**, com o objetivo de aplicar conceitos de programação em **Python**, análise de dados em **R**, integração com **API meteorológica** e versionamento colaborativo utilizando **Git e GitHub**.

---

## 👥 Integrantes

- Matheus Souza Santos
- Andrei Lourenço
- João Vitor Meneses
- Murilo Franco
- Lucas Lima

---

## 📌 Sobre o projeto

A **FarmTech Solutions** é uma aplicação desenvolvida para auxiliar no gerenciamento de culturas agrícolas.

O sistema permite cadastrar e administrar áreas de plantio de **Soja** e **Milho**, calcular automaticamente suas áreas, realizar cálculos relacionados ao manejo de insumos e exportar os dados para um arquivo CSV.

Posteriormente, os dados gerados pelo programa Python são utilizados por scripts em **R** para realização de análises estatísticas.

O projeto também conta com uma integração com a API pública **Open-Meteo**, utilizada para consultar informações meteorológicas em tempo real.

---

## 🌾 Culturas utilizadas

O projeto trabalha com duas culturas agrícolas:

### Soja

Para a soja foi considerado um plantio em formato **circular**, representando um sistema de pivô central.

A área é calculada utilizando:

```text
Área = π × raio²
```

### Milho

Para o milho foi considerado um talhão em formato **retangular**.

A área é calculada utilizando:

```text
Área = comprimento × largura
```

Todas as áreas são armazenadas em **metros quadrados (m²)**.

---

# ⚙️ Funcionalidades

## 🐍 Aplicação em Python

O programa principal apresenta o seguinte menu:

```text
---------- FARMTECH SOLUTIONS ----------

1. Cadastrar plantio
2. Consultar plantios
3. Atualizar plantio
4. Excluir plantio
5. Calcular manejo de insumos
6. Sair
```

### 1. Cadastrar plantio

Permite cadastrar um novo plantio informando:

- Nome do plantio
- Cultura
- Dimensões da área

Dependendo da cultura escolhida, o programa solicita diferentes informações.

**Soja:**

- Raio do pivô

**Milho:**

- Comprimento do talhão
- Largura do talhão

A área é calculada automaticamente pelo sistema.

---

### 2. Consultar plantios

Exibe todos os plantios cadastrados contendo informações como:

- Nome
- Cultura
- Área
- Insumo utilizado
- Quantidade de insumo necessária

---

### 3. Atualizar plantio

Permite modificar dados de um plantio já cadastrado.

É possível alterar:

- Nome do plantio
- Cultura e dimensões da área
- Manejo de insumos

Caso a cultura ou as dimensões sejam alteradas, o sistema recalcula a área automaticamente.

O manejo de insumos anterior também é removido quando necessário para evitar inconsistências nos dados.

---

### 4. Excluir plantio

Permite selecionar e remover um plantio cadastrado.

Além do nome do plantio, todos os dados associados àquela posição dos vetores também são removidos.

---

### 5. Calcular manejo de insumos

O sistema possui sugestões de insumos de acordo com a cultura selecionada.

Entre os insumos disponíveis estão:

#### Soja

- Fungicida
- Herbicida
- Inseticida
- Fertilizante NPK
- Adubo foliar
- Calcário

#### Milho

- Herbicida
- Fungicida
- Inseticida
- Fertilizante nitrogenado
- Fertilizante NPK
- Calcário

Também é possível informar manualmente outro tipo de insumo.

Para realizar o cálculo, o programa solicita:

- Quantidade aplicada por metro
- Unidade utilizada (`mL/metro` ou `litros/metro`)
- Comprimento de cada rua
- Quantidade de ruas

O cálculo realizado é:

```text
Quantidade total = dose por metro × comprimento da rua × quantidade de ruas
```

Quando a entrada é realizada em mililitros, o resultado também é convertido automaticamente para litros.

---

## 💾 Armazenamento dos dados

Durante a execução do programa, os dados são armazenados utilizando **vetores/listas em Python**, conforme solicitado pela atividade.

Entre os vetores utilizados estão:

```python
plantios
culturas
comprimentos
larguras
raios
areas
insumos
dosagens
```

Cada posição representa os dados correspondentes a um mesmo plantio.

Ao selecionar a opção **6 - Sair**, o programa organiza os dados utilizando a biblioteca **Pandas** e gera o arquivo:

```text
dados_fazenda.csv
```

O CSV contém as seguintes colunas:

```text
Nome Plantio
Cultura
Insumo
Dosagem
Comprimento
Largura
Raio
Area
```

Esse arquivo é posteriormente utilizado pela aplicação em R.

---

# 📊 Análise estatística em R

O arquivo:

```text
analise_estatistica.r
```

é responsável por importar os dados armazenados em:

```text
dados_fazenda.csv
```

Antes de iniciar a análise, o programa verifica se o arquivo CSV existe.

Caso não exista, é exibida uma mensagem solicitando que a aplicação Python seja executada primeiro.

São calculadas estatísticas relacionadas às áreas dos plantios e ao manejo de insumos.

### Área plantada

O programa calcula:

- Média das áreas
- Desvio padrão das áreas

### Manejo de insumos

Também são calculados:

- Média da quantidade de insumos
- Desvio padrão da quantidade de insumos

Os resultados são exibidos diretamente no terminal.

---

# 🌦️ API Meteorológica

Como funcionalidade adicional da atividade, foi implementada uma integração em **R** com a API pública:

**Open-Meteo**

Arquivo responsável:

```text
clima_api.r
```

A aplicação realiza uma requisição HTTP para obter informações meteorológicas atuais.

Entre os dados apresentados estão:

- Localização
- Temperatura atual
- Condição meteorológica
- Velocidade do vento
- Direção do vento

As coordenadas podem ser alteradas no código para representar a localização desejada da fazenda.

A integração utiliza as bibliotecas:

```r
httr
jsonlite
```

---

# 📁 Estrutura do projeto

```text
Cap1-FarmTechSolutions-FIAP/
│
├── main.py
│   └── Sistema principal de gerenciamento da fazenda
│
├── dados_fazenda.csv
│   └── Dados exportados pela aplicação Python
│
├── analise_estatistica.r
│   └── Análise estatística dos dados da fazenda
│
├── clima_api.r
│   └── Integração com a API meteorológica Open-Meteo
│
├── main_analise.r
│   └── Arquivo responsável por executar os scripts em R
│
└── README.md
    └── Documentação do projeto
```

---

# 🛠️ Tecnologias utilizadas

### Python

- Python 3
- Pandas
- Math

### R

- R
- httr
- jsonlite

### Outras ferramentas

- Git
- GitHub
- CSV
- Open-Meteo API

---

# 🚀 Como executar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/matheussouzasantos/Cap1-FarmTechSolutions-FIAP.git
```

Entre na pasta do projeto:

```bash
cd Cap1-FarmTechSolutions-FIAP
```

---

## 2. Instalar o Python

É recomendado utilizar **Python 3.10 ou superior**.

Verifique a instalação:

```bash
python --version
```

ou:

```bash
python3 --version
```

---

## 3. Instalar as dependências Python

O projeto utiliza a biblioteca Pandas.

```bash
pip install pandas
```

---

## 4. Executar a aplicação Python

No terminal:

```bash
python main.py
```

Realize os cadastros e cálculos desejados.

Ao terminar, selecione:

```text
6. Sair
```

O programa irá gerar automaticamente:

```text
dados_fazenda.csv
```

---

# 📈 Executando a aplicação em R

## 1. Verificar a instalação do R

```bash
Rscript --version
```

---

## 2. Instalar as bibliotecas necessárias

Abra o R ou RStudio e execute:

```r
install.packages("httr")
install.packages("jsonlite")
```

---

## 3. Executar a análise estatística

Depois de executar o programa Python e gerar o arquivo `dados_fazenda.csv`:

```bash
Rscript analise_estatistica.r
```

O terminal apresentará a média e o desvio padrão das áreas e dos insumos cadastrados.

---

## 4. Executar a consulta meteorológica

```bash
Rscript clima_api.r
```

O programa irá consultar a API Open-Meteo e apresentar as condições meteorológicas atuais.

---

## 5. Executar todos os componentes em R

Também é possível utilizar o arquivo:

```text
main_analise.r
```

para executar os módulos de análise estatística e clima em sequência.

---

# 🔄 Fluxo de funcionamento

```text
Usuário
   │
   ▼
main.py
   │
   ├── Cadastro dos plantios
   ├── Cálculo das áreas
   ├── Manejo de insumos
   ├── Consulta / Atualização / Exclusão
   │
   ▼
dados_fazenda.csv
   │
   ▼
Aplicação em R
   │
   ├── analise_estatistica.r
   │       ├── Média das áreas
   │       └── Desvio padrão
   │
   └── clima_api.r
           └── Open-Meteo API
```

---

# 🧠 Conceitos aplicados

Durante o desenvolvimento foram aplicados conceitos como:

- Variáveis
- Vetores/Listas
- Estruturas condicionais
- Estruturas de repetição
- `match/case`
- Funções
- Tratamento de exceções
- Manipulação de dados
- Operações matemáticas
- Leitura e escrita de arquivos CSV
- DataFrames com Pandas
- Análise estatística
- Requisições HTTP
- Consumo de APIs REST
- Processamento de JSON
- Versionamento de código
- Desenvolvimento colaborativo com Git e GitHub

---

# 🎓 Contexto acadêmico

Este projeto foi desenvolvido como atividade da **FIAP**, simulando o desenvolvimento de uma solução para a startup fictícia **FarmTech Solutions**.

O objetivo da atividade é aplicar conceitos de desenvolvimento de software a um cenário de **Agricultura Digital**, utilizando Python para gerenciamento e processamento dos dados e R para análises estatísticas e integração com serviços externos.

---

## 🔗 Repositório

GitHub:

```text
https://github.com/matheussouzasantos/Cap1-FarmTechSolutions-FIAP
```

---

## 📚 FIAP — Inteligência Artificial

Projeto acadêmico desenvolvido para fins educacionais.