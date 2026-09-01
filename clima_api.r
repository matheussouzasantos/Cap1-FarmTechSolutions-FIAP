# ==============================================================================
# FIAP - FarmTech Solutions
# Componente: Integração com API Meteorológica (Dev: Andrei - Pessoa 4)
# API Utilizada: Open-Meteo (https://open-meteo.com/)
# ==============================================================================

library(httr)
library(jsonlite)

obter_clima_fazenda <- function(latitude = -12.9711, longitude = -38.5108, nome_local = "Salvador / Região") {
  
  cat("=========================================================\n")
  cat("        FARMTECH SOLUTIONS - MONITORAMENTO CLIMÁTICO    \n")
  cat("=========================================================\n")
  cat(sprintf("Buscando dados em tempo real para: %s...\n", nome_local))
  
  # 1. Construir URL de consulta (solicitando temperatura, umidade e vento atuais)
  url_base <- "https://api.open-meteo.com/v1/forecast"
  url_final <- sprintf(
    "%s?latitude=%.4f&longitude=%.4f&current_weather=true&hourly=relative_humidity_2m",
    url_base, latitude, longitude
  )
  
  # 2. Fazer a requisição HTTP GET
  resposta <- GET(url_final)
  
  # 3. Validar se a requisição foi bem-sucedida (Status 200)
  if (status_code(resposta) == 200) {
    # Converter o JSON recebido para uma lista do R
    conteudo <- content(resposta, as = "text", encoding = "UTF-8")
    dados_clima <- fromJSON(conteudo)
    
    # Extrair dados do tempo atual
    tempo_atual  <- dados_clima$current_weather
    temperatura  <- tempo_atual$temperature
    val_vento    <- tempo_atual$windspeed
    dir_vento    <- tempo_atual$winddirection
    codigo_tempo <- tempo_atual$weathercode
    
    # Mapeamento simples de códigos meteorológicos WMO
    condicao_texto <- switch(
      as.character(codigo_tempo),
      "0" = "Céu Limpo / Ensolarado",
      "1" = "Predominantemente Limpo",
      "2" = "Parcialmente Nublado",
      "3" = "Encoberto",
      "45" = "Névoa",
      "51" = "Garoa Leve",
      "61" = "Chuva Leve",
      "63" = "Chuva Moderada",
      "80" = "Pancadas de Chuva",
      "Tempo Variável / Verificar Boletim"
    )
    
    # 4. Exibir resultados formatados no Terminal
    cat("\n--> CONDIÇÕES METEOROLÓGICAS ATUAIS:\n")
    cat(sprintf("   • Localização:           %s (Lat: %.2f, Lon: %.2f)\n", nome_local, latitude, longitude))
    cat(sprintf("   • Temperatura Atual:     %.1f °C\n", temperatura))
    cat(sprintf("   • Condição do Tempo:     %s\n", condicao_texto))
    cat(sprintf("   • Velocidade do Vento:   %.1f km/h\n", val_vento))
    cat(sprintf("   • Direção do Vento:      %d°\n", dir_vento))
    cat("=========================================================\n")
    
  } else {
    cat("ERRO: Não foi possível conectar à API de Clima.\n")
    cat(sprintf("Status Code: %d\n", status_code(resposta)))
    cat("=========================================================\n")
  }
}

# Executar a função (pode alterar as coordenadas para a fazenda real)
obter_clima_fazenda()