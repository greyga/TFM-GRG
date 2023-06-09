# -*- coding: utf-8 -*-
"""OBTAINHPOVCF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cMps6Db_AqWgrl9YQBMbdBAm5YZQONze
"""

if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("TxDb.Hsapiens.UCSC.hg19.knownGene")

if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("org.Hs.eg.db")

library(AnnotationDbi)
library(org.Hs.eg.db)
gene_id <- select(org.Hs.eg.db, keys="ADA", keytype="SYMBOL", columns="ENTREZID")
gene_id

library(TxDb.Hsapiens.UCSC.hg19.knownGene)
library(org.Hs.eg.db)

# Obtener el Entrez ID de ADA
ada_entrez <- as.character(org.Hs.egSYMBOL2EG["ADA"])

# Crear una conexión a la base de datos de la librería TxDb.Hsapiens.UCSC.hg19.knownGene
txdb <- TxDb.Hsapiens.UCSC.hg19.knownGene

# Obtener las coordenadas cromosómicas del gen ADA
ada_coords <- select(txdb, keys = ada_entrez, columns = c("TXCHROM", "TXSTART", "TXEND"), keytype = "GENEID")
ada_coords

library(org.Hs.eg.db)
library(TxDb.Hsapiens.UCSC.hg19.knownGene)

# Obtener los Entrez ID de los genes de interés
gene_symbols <- c("GP9", "SLC27A4", "CARD10", "IL21R", "RIC1", "DUOX2", "GLIS3", "LHX3", "THRB", "TPO", "ALG8")
entrez_ids <- select(org.Hs.eg.db, keys=gene_symbols, keytype="SYMBOL", columns="ENTREZID")

# Crear una conexión a la base de datos de la librería TxDb.Hsapiens.UCSC.hg19.knownGene
txdb <- TxDb.Hsapiens.UCSC.hg19.knownGene

# Obtener las coordenadas cromosómicas de los genes de interés
gene_coords <- select(txdb, keys = entrez_ids$ENTREZID, columns = c("TXCHROM", "TXSTART", "TXEND"), keytype = "GENEID")
gene_coords

if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("VariantAnnotation")
library(VariantAnnotation)

library(VariantAnnotation)

# Descargar el archivo VCF de Clinvar
download.file("https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz",
              destfile = "clinvar.vcf.gz")

install.packages("R.utils")

# Cargar el archivo vcf
vcf_file <- "clinvar.vcf.gz"

# Abrir el archivo comprimido
vcf_gz <- gzfile(vcf_file, "r")

# Leer el archivo vcf
vcf <- readLines(vcf_gz)

# Cerrar el archivo
close(vcf_gz)

# Guardar el archivo descomprimido
writeLines(vcf, "clinvar.vcf")

# Cargar el archivo VCF
vcf_file <- "clinvar.vcf"

# Leer el archivo VCF usando readLines
vcf_lines <- readLines(gzfile(vcf_file))

# Obtener índices de las líneas que corresponden a variantes del cromosoma 20
chr20_variants_idx <- grep("^20\t", vcf_lines)

# Filtrar las variantes del cromosoma 20 que están en el rango de posiciones
chr20_filtered_idx <- which(
  sapply(strsplit(vcf_lines[chr20_variants_idx], "\t"), function(x) {
    chrom <- x[1]
    pos <- as.numeric(x[2])
    chrom == "20" & pos >= 43248163 & pos <= 43280376
  })
)

# Imprimir las líneas que corresponden a las variantes del cromosoma 20 y en el rango de posiciones
cat(vcf_lines[chr20_variants_idx][chr20_filtered_idx], sep = "\n")

# funcion para filtrar VCF por intervalor cromosomico
filter_vcf_by_positions <- function(vcf_file, positions) {
  # Cargar el archivo VCF
  vcf_lines <- readLines(gzfile(vcf_file))

  # Recorrer todas las posiciones cromosómicas y aplicar el filtro a cada una
  filtered_indices <- lapply(positions, function(pos) {
    chrom <- pos$chrom
    start <- as.numeric(pos$start)
    end <- as.numeric(pos$end)
    chrom_variants_idx <- grep(paste0("^", chrom, "\t"), vcf_lines)
    chr_filtered_idx <- which(vapply(strsplit(vcf_lines[chrom_variants_idx], "\t"), function(x) {
      chrom_vcf <- x[1]
      pos_vcf <- as.numeric(x[2])
      chrom_vcf == chrom & pos_vcf >= start & pos_vcf <= end
    }, logical(1)))
    chrom_variants_idx[chr_filtered_idx]
  })

  # Combinar los índices de variantes filtradas de todas las posiciones cromosómicas
  combined_indices <- unique(unlist(filtered_indices))

  # Imprimir las líneas que corresponden a las variantes filtradas
  cat(vcf_lines[combined_indices], sep = "\n")
}

# Definir las posiciones cromosómicas a filtrar
positions <- list(
  list(chrom = "3", start = 128779645, end = 128781253), 		
  list(chrom = "9", start = 131102839, end = 131123749),
  list(chrom = "22", start = 37875383, end = 37915378),
  list(chrom = "15", start = 45384852, end = 45406359),
  list(chrom = "9", start = 3824128, end = 3937189),
  list(chrom = "9", start = 139088096, end = 139095004),
  list(chrom = "3", start = 24158645, end = 24536313),
  list(chrom = "2", start = 1377995, end = 1546499),
  list(chrom = "11", start = 77811988, end = 77850699),
  list(chrom = "16", start = 27413483, end = 27463363),
  list(chrom = "9", start = 5629119, end = 5769454)
)

# Filtrar el archivo VCF por las posiciones cromosómicas especificadas
filter_vcf_by_positions("clinvar.vcf", positions)