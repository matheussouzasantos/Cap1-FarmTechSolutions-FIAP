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
  
  # --- TRATAMENTO DAS COLUNAS (Compatibilidade com o Python do Matheus) ---
  
  # Identificar a coluna de Área (pode vir como 'Area' ou 'area_m2')
  col_area <- if ("Area" %in% colnames(dados)) dados$Area else dados$area_m2
  
  # Garantir que os dados da Área sejam numéricos
  col_area <- as.numeric(col_area)
  
  # Identificar a coluna de Insumos (se não existir 'total_insumo_litros', usa 'Dosagem')
  if ("total_insumo_litros" %in% colnames(dados)) {
    col_insumo <- as.numeric(dados$total_insumo_litros)
  } else if ("Dosagem" %in% colnames(dados)) {
    col_insumo <- as.numeric(dados$Dosagem)
  } else {
    col_insumo <- c(0)
  }
  
  # 4. Cálculo de Média e Desvio Padrão - ÁREA (m²)
  media_area <- mean(col_area, na.rm = TRUE)
  dp_area    <- sd(col_area, na.rm = TRUE)
  
  # Se houver apenas 1 registro ou valores iguais, o desvio padrão pode vir NA
  if (is.na(dp_area)) dp_area <- 0
  
  cat("--> ESTATÍSTICAS DE ÁREA PLANTADA (m²):\n")
  cat(sprintf("   • Média das Áreas:          %.2f m²\n", media_area))
  cat(sprintf("   • Desvio Padrão das Áreas:  %.2f m²\n", dp_area))
  cat("---------------------------------------------------------\n")
  
  # 5. Cálculo de Média e Desvio Padrão - INSUMOS
  media_insumo <- mean(col_insumo, na.rm = TRUE)
  dp_insumo    <- sd(col_insumo, na.rm = TRUE)
  
  if (is.na(dp_insumo)) dp_insumo <- 0
  
  cat("--> ESTATÍSTICAS DE MANEJO DE INSUMOS:\n")
  cat(sprintf("   • Média de Insumos:         %.2f\n", media_insumo))
  cat(sprintf("   • Desvio Padrão de Insumos: %.2f\n", dp_insumo))
  cat("=========================================================\n")
}
