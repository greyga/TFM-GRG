# -*- coding: utf-8 -*-
"""TRATAMIENTO DATOS+genes

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X_JADqz2Vqx_bKeMgSCPd1ECJCVsi1CA
"""

library(dplyr)

# Cargar el archivo CSV
data <- read.csv("/content/DATOS COMPARACION - DATOS PRUEBA.csv", sep = ",", header = TRUE)

# Crear una lista vacía para almacenar los resultados
resultados <- list()

# Obtener la lista de variantes
variantes <- c("GP9", "SLC27A4", "CARD10", "DUOX2", "GLIS3", "LHX3", "THRB", "TPO", "ALG8", "IL21R", "RIC1")

# Recorrer cada variante y extraer el ranking y Phenotypic Score correspondientes
for (variante in variantes) {
  subset_data <- subset(data, Ab_immune_system == variante)
  
  # Obtener el ranking y Phenotypic Score de la variante
  ranking <- subset_data$Ranking[!is.na(subset_data$Ranking)]
  ps_estrategia <- subset_data$PS_AIGS[!is.na(subset_data$PS_AIGS)]
  
  # Verificar si hay valores válidos para la variante y estrategia
  if (length(ranking) > 0 && length(ps_estrategia) > 0) {
    # Crear un dataframe con los datos de ranking y Phenotypic Score
    df <- data.frame(Variante = variante, Ranking = ranking, Phenotypic_Score = ps_estrategia)
    
    # Agregar el dataframe a la lista de resultados
    resultados[[variante]] <- df
  }
}

# Combinar los dataframes en una única tabla
tabla_resultados <- bind_rows(resultados)

# Imprimir la tabla de resultados   
print(tabla_resultados)

# Obtener la lista de variantes
variantes <- c("GP9", "SLC27A4", "CARD10","IL21R", "RIC1")
# Recorrer cada variante y extraer el ranking y Phenotypic Score correspondientes
for (variante in variantes) {
  subset_data <- subset(data, Ab_immune_system == variante)
  
  # Obtener el ranking y Phenotypic Score de la variante
  ranking <- subset_data$Ranking[!is.na(subset_data$Ranking)]
  ps_estrategia <- subset_data$PS_AIGS[!is.na(subset_data$PS_AIGS)]
  
  # Verificar si hay valores válidos para la variante y estrategia
  if (length(ranking) > 0 && length(ps_estrategia) > 0) {
    # Crear un dataframe con los datos de ranking y Phenotypic Score
    df <- data.frame(Variante = variante, Ranking = ranking, Phenotypic_Score = ps_estrategia)
    
    # Agregar el dataframe a la lista de resultados
    resultados[[variante]] <- df
  }
}

# Combinar los dataframes en una única tabla
tabla_resultados <- bind_rows(resultados)

# Imprimir la tabla de resultados   
print(tabla_resultados)

library(dplyr)

# Cargar el archivo CSV
data <- read.csv("/content/DATOS COMPARACION - DATOS PRUEBA.csv", sep = ",", header = TRUE)

# Crear una lista vacía para almacenar los resultados
resultados <- list()

# Definir las estrategias y sus respectivas columnas de Phenotypic Score
estrategias <- c("Sin_HPO", "Asthma", "Asthma_ARS", "Asthma_ARP", "Ab_Resp_system", "Asthma_Ig_hypers", "Asthma_Abnormality_Igsystem", "Ab_immune_system", "Decreased_T4", "Decreased_T4_Abnormal_circulating_T4_concentration", "Increased_T4", "HPO increased T4_Abnormal_T4", "Ab_endocrine_system", "all_HPOS", "Abnormality_of_face")

columnas_ps <- c("PS_Sin_HPO", "PS_Asthma", "PS_A_Ab_Resp", "PS_A_y_ARP", "PS_ARS", "PS_A_y_Ighypers", "PS_A_AIGS", "PS_AIGS",
                 "PS_Decreased_T4", "PS_dT4_ACT4", "PS_iT4", "PS_dT4_ACT4", "PS_AES", "PS_allHPO", "PS_AOF")

# Recorrer cada estrategia
for (i in seq_along(estrategias)) {
  estrategia <- estrategias[i]
  columna_ps <- columnas_ps[i]
  
  # Recorrer cada variante y extraer el ranking y Phenotypic Score correspondientes
  for (variante in variantes) {
    subset_data <- subset(data, data[[estrategia]] == variante)
    
    # Obtener el ranking y Phenotypic Score de la variante y estrategia
    ranking <- subset_data$Ranking[!is.na(subset_data$Ranking)]
    ps_estrategia <- subset_data[[columna_ps]][!is.na(subset_data[[columna_ps]])]
    
    # Verificar si hay valores válidos para la variante y estrategia
    if (length(ranking) > 0 && length(ps_estrategia) > 0) {
      # Convertir la columna de Phenotypic Score a tipo "character"
      ps_estrategia <- as.character(ps_estrategia)
      
      # Crear un dataframe con los datos de ranking y Phenotypic Score
      df <- data.frame(Variante = variante, Estrategia = estrategia, Ranking = ranking, Phenotypic_Score = ps_estrategia)
      
      # Agregar el dataframe a la lista de resultados
      resultados[[paste(variante, estrategia, sep = "_")]] <- df
    }
  }
}

# Combinar los dataframes en una única tabla
tabla_resultados <- bind_rows(resultados)

# Imprimir la tabla de resultados
print(tabla_resultados)

# Verificar el tipo de variables en tabla_resultados
str(tabla_resultados)

tabla_resultados$Ranking <- as.numeric(gsub(",", ".", tabla_resultados$Ranking))
tabla_resultados$Phenotypic_Score <- as.numeric(gsub(",", ".", tabla_resultados$Phenotypic_Score))

# Crear el DataFrame "datos_Asthma"
datos_Asthma <- data.frame(
  Variante = c("GP9", "SLC27A4", "CARD10", "DUOX2", "GLIS3", "LHX3", "THRB", "TPO", "ALG8", "IL21R", "RIC1"),
  Ranking = c(17, 1, 2, 5, 18, 4, 8, 15, 7, 21, 3),
  Phenotypic_Score = c(1.00, 0.85, 0.69, 0.51, 0.51, 0.51, 0.50, 0.50, 0.50, 0.61, 1.00),
  stringsAsFactors = FALSE
)

# Imprimir el DataFrame "datos_Asthma"
print(datos_Asthma)

str(datos_Asthma)

# Crear el DataFrame "datos_Sin_HPO"
datos_Sin_HPO <- data.frame(
  Variante = c("GP9", "SLC27A4", "CARD10", "DUOX2", "GLIS3", "LHX3", "THRB", "TPO", "ALG8", "IL21R", "RIC1"),
  Ranking = c(20, 5, 9, 3, 18, 4, 6, 17, 2, 21, 19),
  Phenotypic_Score = rep(0, 11),
  stringsAsFactors = FALSE
)

# Imprimir el DataFrame "datos_Sin_HPO"
print(datos_Sin_HPO)

# Crear el DataFrame "datos_Asthma_ARS"
datos_Asthma_ARS <- data.frame(
  Variante = c("GP9", "SLC27A4", "CARD10", "DUOX2", "GLIS3", "LHX3", "THRB", "TPO", "ALG8", "IL21R", "RIC1"),
  Ranking = c(17, 1, 2, 6, 18, 5, 3, 16, 8, 21, 4),
  Phenotypic_Score = c(1, 1, 0.87, 0.51, 0.51, 0.53, 0.76, 0.5, 0.51, 0.71, 1),
  stringsAsFactors = FALSE
)

# Imprimir el DataFrame "datos_Asthma_ARS"
print(datos_Asthma_ARS)

# Crear el DataFrame "datos_Asthma_ARP"
datos_Asthma_ARP <- data.frame(
  Variante = c("GP9", "SLC27A4", "CARD10", "DUOX2", "GLIS3", "LHX3", "THRB", "TPO", "ALG8", "IL21R", "RIC1"),
  Ranking = c(17, 1, 2, 8, 18, 6, 3, 15, 9, 21, 5),
  Phenotypic_Score = c(0.99, 0.92, 0.74, 0.5, 0.51, 0.53, 0.66, 0.5, 0.5, 0.55, 0.99),
  stringsAsFactors = FALSE
)

# Imprimir el DataFrame "datos_Asthma_ARP"
print(datos_Asthma_ARP)

# Crear el DataFrame "datos_Ab_Resp_system"
datos_Ab_Resp_system <- data.frame(
  Variante = c("GP9", "SLC27A4", "CARD10", "DUOX2", "GLIS3", "LHX3", "THRB", "TPO", "ALG8", "IL21R", "RIC1"),
  Ranking = c(19, 1, 8, 4, 15, 3, 2, 14, 5, 20, 21),
  Phenotypic_Score = c(0.5, 1, 0.5, 0.51, 0.51, 0.53, 1, 0.51, 0.51, 0.51, 0),
  stringsAsFactors = FALSE
)

# Imprimir el DataFrame "datos_Ab_Resp_system"
print(datos_Ab_Resp_system)

# Crear el DataFrame "datos_Asthma_Ig_hypers"
datos_Asthma_Ig_hypers <- data.frame(
  Variante = c("GP9", "SLC27A4", "CARD10", "DUOX2", "GLIS3", "LHX3", "THRB", "TPO", "ALG8", "IL21R", "RIC1"),
  Ranking = c(17, 1, 2, 6, 18, 4, 8, 15, 7, 21, 3),
  Phenotypic_Score = c(1, 0.89, 0.69, 0.51, 0.51, 0.51, 0.5, 0.5, 0.5, 0.61, 1),
  stringsAsFactors = FALSE
)

# Imprimir el DataFrame "datos_Asthma_Ig_hypers"
print(datos_Asthma_Ig_hypers)

# Crear el DataFrame "datos_Asthma_Abnormality_Igsystem"
datos_Asthma_Abnormality_Igsystem <- data.frame(
  Variante = c("GP9", "SLC27A4", "CARD10", "GLIS3", "LHX3", "THRB", "TPO", "ALG8", "IL21R", "RIC1"),
  Ranking = c(17, 1, 2, 18, 4, 8, 16, 7, 21, 3),
  Phenotypic_Score = c(0.98, 0.85, 0.72, 0.51, 0.5, 0.5, 0.5, 0.5, 0.66, 0.98),
  stringsAsFactors = FALSE
)

# Imprimir el DataFrame "datos_Asthma_Abnormality_Igsystem"
print(datos_Asthma_Abnormality_Igsystem)

"""CURVAS **ROC**

1. HPO: Asthma HP:0002099
"""

# Crear la variable binaria que indica si una variante está entre las 10 primeras o no
datos_Asthma$Top10 <- ifelse(datos_Asthma$Ranking <= 10, 1, 0)

# Ajustar el modelo de regresión logística para la estrategia "Asthma"
modelo_Asthma <- glm(Top10 ~ Phenotypic_Score, data = datos_Asthma, family = "binomial")

# Calcular las probabilidades predichas de que una variante esté entre las 10 primeras para la estrategia "Asthma"
nuevos_datos_Asthma <- data.frame(Phenotypic_Score = c(0.6, 0.75, 0.95))
probabilidades_Asthma <- predict(modelo_Asthma, newdata = nuevos_datos_Asthma, type = "response")

# Imprimir las probabilidades predichas para la estrategia "Asthma"
cat("Probabilidades para la estrategia 'Asthma':\n")
print(probabilidades_Asthma)

# Obtener las predicciones del modelo para los datos originales
predicciones_Asthma <- predict(modelo_Asthma, type = "response")

# Crear una variable binaria de predicciones (considerando un punto de corte de 0.6)
predicciones_binarias_Asthma <- ifelse(predicciones_Asthma > 0.5, 1, 0)

# Crear una matriz de confusión
matriz_confusion_Asthma <- table(datos_Asthma$Top10, predicciones_binarias_Asthma)
print(matriz_confusion_Asthma)

# Calcular las métricas de desempeño del modelo
accuracy <- sum(diag(matriz_confusion_Asthma)) / sum(matriz_confusion_Asthma)
precision <- matriz_confusion_Asthma[1, 1] / sum(predicciones_binarias_Asthma)
recall <- matriz_confusion_Asthma[2, 1] / sum(datos_Asthma$Top10)
f1_score <- 2 * (precision * recall) / (precision + recall)

cat("Accuracy:", accuracy, "\n")
cat("Precision:", precision, "\n")
cat("Recall:", recall, "\n")
cat("F1 Score:", f1_score, "\n")

# Verificar si la librería pROC está instalada
if (!requireNamespace("pROC", quietly = TRUE)) {
  # Instalar la librería pROC
  install.packages("pROC")
}

# Cargar la librería pROC
library(pROC)

# Obtener las respuestas verdaderas para los datos originales
respuestas_verdaderas_Asthma <- datos_Asthma$Top10

# Calcular la curva ROC
roc_Asthma<- roc(respuestas_verdaderas_Asthma, predicciones_Asthma)

# Plotear la curva ROC
plot(roc_Asthma, main = "Curva ROC - Asthma")
# Calcular el área bajo la curva (AUC)
auc_Asthma <- auc(respuestas_verdaderas_Asthma, predicciones_Asthma)

# Mostrar el AUC
cat("Área bajo la curva (AUC):", auc_Asthma, "\n")

"""2. HPO: Asthma HP:0002099 + Abnormality of the respiratory system HP:0002086"""

# Crear la variable binaria que indica si una variante está entre las 10 primeras o no
datos_Asthma_ARS$Top10 <- ifelse(datos_Asthma_ARS$Ranking <= 10, 1, 0)

# Ajustar el modelo de regresión logística para la estrategia "Asthma_ARS"
modelo_Asthma_ARS <- glm(Top10 ~ Phenotypic_Score, data = datos_Asthma_ARS, family = "binomial")

# Calcular las probabilidades predichas de que una variante esté entre las 10 primeras para la estrategia "Asthma_ARS"
nuevos_datos_Asthma_ARS <- data.frame(Phenotypic_Score = c(0.25, 0.75, 0.95))
probabilidades_Asthma_ARS <- predict(modelo_Asthma_ARS, newdata = nuevos_datos_Asthma_ARS, type = "response")

# Imprimir las probabilidades predichas para la estrategia "Asthma_ARS"
cat("Probabilidades para la estrategia 'Asthma_ARS':\n")
print(probabilidades_Asthma_ARS)

# Obtener las predicciones del modelo para los datos originales
predicciones_Asthma_ARS <- predict(modelo_Asthma_ARS, type = "response")

# Crear una variable binaria de predicciones (considerando un punto de corte de 0.6)
predicciones_binarias_Asthma_ARS <- ifelse(predicciones_Asthma_ARS > 0.6, 1, 0)

# Crear una matriz de confusión
matriz_confusion_Asthma_ARS <- table(datos_Asthma_ARS$Top10, predicciones_binarias_Asthma_ARS)
print(matriz_confusion_Asthma_ARS)

# Calcular las métricas de desempeño del modelo
accuracy <- sum(diag(matriz_confusion_Asthma_ARS)) / sum(matriz_confusion_Asthma_ARS)
precision <- matriz_confusion_Asthma_ARS[2, 2] / sum(predicciones_binarias_Asthma_ARS)
recall <- matriz_confusion_Asthma_ARS[2, 2] / sum(datos_Asthma_ARS$Top10)
f1_score <- 2 * (precision * recall) / (precision + recall)

cat("Accuracy:", accuracy, "\n")
cat("Precision:", precision, "\n")
cat("Recall:", recall, "\n")
cat("F1 Score:", f1_score, "\n")

# Verificar si la librería pROC está instalada
if (!requireNamespace("pROC", quietly = TRUE)) {
  # Instalar la librería pROC
  install.packages("pROC")
}

# Cargar la librería pROC
library(pROC)

# Obtener las respuestas verdaderas para los datos originales
respuestas_verdaderas_Asthma_ARS <- datos_Asthma_ARS$Top10

# Calcular la curva ROC
roc_Asthma_ARS <- roc(respuestas_verdaderas_Asthma_ARS, predicciones_Asthma_ARS)

# Plotear la curva ROC
plot(roc_Asthma_ARS, main = "Curva ROC - Asthma_ARS")

# Calcular el área bajo la curva (AUC)
auc_Asthma_ARS <- auc(respuestas_verdaderas_Asthma_ARS, predicciones_Asthma_ARS)

# Mostrar el AUC
cat("Área bajo la curva (AUC):", auc_Asthma_ARS, "\n")



# Crear la variable binaria que indica si una variante está entre las 10 primeras o no
datos_Ab_Resp_system$Top10 <- ifelse(datos_Ab_Resp_system$Ranking <= 10, 1, 0)

# Ajustar el modelo de regresión logística para la estrategia "Ab_Resp_system"
modelo_Ab_Resp_system <- glm(Top10 ~ Phenotypic_Score, data = datos_Ab_Resp_system, family = "binomial")

# Calcular las probabilidades predichas de que una variante esté entre las 10 primeras para la estrategia "Ab_Resp_system"
nuevos_datos_Ab_Resp_system <- data.frame(Phenotypic_Score = c(0.25, 0.75, 0.95))
probabilidades_Ab_Resp_system <- predict(modelo_Ab_Resp_system, newdata = nuevos_datos_Ab_Resp_system, type = "response")

# Imprimir las probabilidades predichas para la estrategia "Ab_Resp_system"
cat("Probabilidades para la estrategia 'Ab_Resp_system':\n")
print(probabilidades_Ab_Resp_system)

# Verificar si la librería pROC está instalada
if (!requireNamespace("pROC", quietly = TRUE)) {
  # Instalar la librería pROC
  install.packages("pROC")
}

# Cargar la librería pROC
library(pROC)

# Obtener las predicciones del modelo para los datos originales
predicciones_Ab_Resp_system <- predict(modelo_Ab_Resp_system, type = "response")

# Crear una variable binaria de predicciones (considerando un punto de corte de 0.5)
predicciones_binarias_Ab_Resp_system <- ifelse(predicciones_Ab_Resp_system > 0.5, 1, 0)

# Crear una matriz de confusión
matriz_confusion_Ab_Resp_system <- table(datos_Ab_Resp_system$Top10, predicciones_binarias_Ab_Resp_system)
print(matriz_confusion_Ab_Resp_system)

# Calcular las métricas de desempeño del modelo
accuracy <- sum(diag(matriz_confusion_Ab_Resp_system)) / sum(matriz_confusion_Ab_Resp_system)
precision <- matriz_confusion_Ab_Resp_system[2, 2] / sum(predicciones_binarias_Ab_Resp_system)
recall <- matriz_confusion_Ab_Resp_system[2, 2] / sum(datos_Ab_Resp_system$Top10)
f1_score <- 2 * (precision * recall) / (precision + recall)

cat("Accuracy:", accuracy, "\n")
cat("Precision:", precision, "\n")
cat("Recall:", recall, "\n")
cat("F1 Score:", f1_score, "\n")

# Obtener las respuestas verdaderas para los datos originales
respuestas_verdaderas_Ab_Resp_system <- datos_Ab_Resp_system$Top10

# Calcular la curva ROC
roc_Ab_Resp_system <- roc(respuestas_verdaderas_Ab_Resp_system, predicciones_Ab_Resp_system)

# Plotear la curva ROC
plot(roc_Ab_Resp_system, main = "Curva ROC - Ab_Resp_system")
# Calcular el área bajo la curva (AUC)
auc_Ab_Resp_system <- auc(respuestas_verdaderas_Ab_Resp_system, predicciones_Ab_Resp_system)

# Mostrar el AUC
cat("Área bajo la curva (AUC):", auc_Ab_Resp_system, "\n")

# Tramar la primera curva ROC
plot(roc_Ab_Resp_system, col = "red", lty = 1, main = "Curvas ROC", xlab = "Tasa de Falsos Positivos", ylab = "Tasa de Verdaderos Positivos")

# Agregar las otras curvas ROC
lines(roc_Asthma_ARS, col = "blue", lty = 2)
lines(roc_Asthma, col = "green", lty = 3)

# Mostrar los AUC en una leyenda
legend("bottomright", legend = c(paste("AUC Ab_Resp_system =", auc_Ab_Resp_system),
                                paste("AUC Asthma_ARS =", auc_Asthma_ARS),
                                paste("AUC Asthma =", auc_Asthma)),
       col = c("red", "blue", "green"), lty = c(1, 2, 3), bty = "n")

library(ggplot2)

# Gráfico de barras del ranking para una variante específica
variante <- "GP9"  # Variante específica que deseas analizar
subset_tabla <- subset(tabla_resultados, Variante == variante)

# Crear el gráfico de barras
ggplot(subset_tabla, aes(x = Estrategia, y = Ranking)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = paste("Variante:", variante), x = "Estrategia", y = "Ranking")

library(ggplot2)

# Gráfico de dispersión del ranking y puntaje fenotípico para todas las variantes
ggplot(tabla_resultados, aes(x = Ranking, y = Phenotypic_Score, color = Estrategia)) +
  geom_point() +
  labs(title = "Relación entre Ranking y Phenotypic Score", x = "Ranking", y = "Phenotypic Score")

# ANOVA de dos factores para el ranking
anova_ranking <- aov(Ranking ~ Variante + Estrategia, data = tabla_resultados)
summary(anova_ranking)

"""En este caso, se observa lo siguiente:

Variante: El valor de p es menor que 0.001 (***), lo que indica que hay diferencias significativas en el ranking entre las variantes. Esto significa que las variantes tienen un impacto significativo en el ranking.

Estrategia: El valor de p es 0.835 (> 0.05), lo que indica que no hay diferencias significativas en el ranking entre las estrategias. Esto significa que las estrategias utilizadas no tienen un impacto significativo en el ranking.

Residuals: Representa la variabilidad no explicada por los factores. En este caso, se obtiene una suma de cuadrados de 1220 y un promedio de cuadrados de 12.3.

En resumen, el análisis indica que las variantes tienen un efecto significativo en el ranking, mientras que las estrategias utilizadas no muestran diferencias significativas en el ranking.
"""

data <- data.frame(
  Variantes = c("GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "GP9", "SLC27A4", "CARD10", "IL21R", "RIC1")
  Estrategia = c("Sin_HPO", "Sin_HPO", "Sin_HPO", "Sin_HPO", "Sin_HPO", "Asthma", "Asthma", "Asthma", "Asthma", "Asthma", "Asthma_ARS", "Asthma_ARS", "Asthma_ARS", "Asthma_ARS", "Asthma_ARS", "Asthma_ARP", "Asthma_ARP", "Asthma_ARP", "Asthma_ARP", "Asthma_ARP", "Ab_Resp_system", "Ab_Resp_system", "Ab_Resp_system", "Ab_Resp_system", "Ab_Resp_system", "Asthma_Ig_hypers", "Asthma_Ig_hypers", "Asthma_Ig_hypers", "Asthma_Ig_hypers", "Asthma_Ig_hypers", "Asthma_Abnormality_Igsystem", "Asthma_Abnormality_Igsystem", "Asthma_Abnormality_Igsystem", "Asthma_Abnormality_Igsystem", "Asthma_Abnormality_Igsystem", "Ab_immune_system", "Ab_immune_system", "Ab_immune_system", "Ab_immune_system", "Ab_immune_system", "Decreased_T4", "Decreased_T4", "Decreased_T4", "Decreased_T4", "Decreased_T4", "Increased_T4", "Increased_T4", "Increased_T4", "Increased_T4", "Increased_T4", "Ab_endocrine_system", "Ab_endocrine_system", "Ab_endocrine_system", "Ab_endocrine_system", "Ab_endocrine_system", "all_HPOS", "all_HPOS", "all_HPOS", "all_HPOS", "all_HPOS", "Abnormality_of_face", "Abnormality_of_face", "Abnormality_of_face", "Abnormality_of_face", "Abnormality_of_face")
  Ranking = c(20.00, 5.00, 9.00, 21.00, 19.00, 17.00, 1.00, 2.00, 21.00, 3.00, 17.00, 1.00, 2.00, 21.00, 4.00, 17.00, 1.00, 2.00, 21.00, 5.00, 19.00, 1.00, 8.00, 20.00, 21.00, 17.00, 1.00, 2.00, 21.00, 3.00, 17.00, 1.00, 2.00, 21.00, 3.00, 20.00, 5.00, 9.00, 21.00, 19.00, 19.00, 7.00, 9.00, 20.00, 21.00, 19.00, 5.00, 8.00, 20.00, 21.00, 19.00, 7.00, 5.00, 20.00, 21.00, 20.00, 4.00, 5.00, 21.00, 15.00, 20.00, 1.00, 11.00, 17.00, 21.00)
  Phenotypic_Score = c(0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.85, 0.69, 0.61, 1.00, 1.00, 1.00, 0.87, 0.71, 1.00, 0.99, 0.92, 0.74, 0.55, 0.99, 0.50, 1.00, 0.50, 0.51, 0.00, 1.00, 0.89, 0.69, 0.61, 1.00, 0.98, 0.85, 0.72, 0.66, 0.98, 0.00, 0.00, 0.00, 0.00, 0.00, 0.50, 0.50, 0.50, 0.50, 0.00, 0.50, 0.50, 0.50, 0.50, 0.00, 0.50, 0.50, 0.51, 0.50, 0.00, 0.50, 0.67, 0.65, 0.50, 0.62, 0.52, 1.00, 0.50, 1.00, 0.00))