# ==============================================================================
# FIAP - FarmTech Solutions
# Componente: Análise Estatística em R (Dev: Andrei - Pessoa 4)
# ==============================================================================

# 1. Definir caminho do arquivo gerado pelo Python
arquivo_csv <- "dados_fazenda.csv"

# 2. Verificar se o arquivo existe antes de carregar
if (!file.exists(arquivo_csv)) {
  cat("=========================================================\n")
  cat("ERRO: O arquivo 'dados_fazenda.csv' nao foi encontrado!\n")
  cat("Execute o programa em Python primeiro para gerar os dados.\n")
  cat("=========================================================\n")
} else {
  
  # 3. Importar dados do CSV
  dados <- read.csv(arquivo_csv, stringsAsFactors = FALSE)
  
  cat("=========================================================\n")
  cat("         FARMTECH SOLUTIONS - RELATÓRIO ESTATÍSTICO      \n")
  cat("=========================================================\n\n")
  
  cat("--> DADOS IMPORTADOS DO PYTHON:\n")
  print(dados)
  cat("\n---------------------------------------------------------\n")
  
  # 4. Cálculo de Média e Desvio Padrão - ÁREA (m²)
  media_area <- mean(dados$area_m2, na.rm = TRUE)
  dp_area    <- sd(dados$area_m2, na.rm = TRUE)
  
  # Tratar caso de desvio padrão em amostras com apenas 1 registro (retorna NA no R)
  if (is.na(dp_area)) dp_area <- 0
  
  cat("--> ESTATÍSTICAS DE ÁREA PLANTADA (m²):\n")
  cat(sprintf("   • Média das Áreas:          %.2f m²\n", media_area))
  cat(sprintf("   • Desvio Padrão das Áreas:  %.2f m²\n", dp_area))
  cat("---------------------------------------------------------\n")
  
  # 5. Cálculo de Média e Desvio Padrão - INSUMOS (Litros)
  media_insumo <- mean(dados$total_insumo_litros, na.rm = TRUE)
  dp_insumo    <- sd(dados$total_insumo_litros, na.rm = TRUE)
  
  if (is.na(dp_insumo)) dp_insumo <- 0
  
  cat("--> ESTATÍSTICAS DE MANEJO DE INSUMOS (Litros):\n")
  cat(sprintf("   • Média de Insumos:         %.2f Litros\n", media_insumo))
  cat(sprintf("   • Desvio Padrão de Insumos: %.2f Litros\n", dp_insumo))
  cat("=========================================================\n")
}