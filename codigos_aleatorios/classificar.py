from pathlib import Path
from collections import Counter
import re


# -------------------------
# CONFIGURAÇÃO
# -------------------------

input_folder = Path("resultado/txt")

stopwords = {
    "a", "o", "as", "os",
    "de", "do", "da", "dos", "das",
    "e", "ou",
    "em", "no", "na", "nos", "nas",
    "um", "uma", "uns", "umas",
    "para", "por",
    "que", "com",
    "se", "ao", "aos"
}


# -------------------------
# LER E ANALISAR ARQUIVOS
# -------------------------

documentos = {}

for arquivo in input_folder.rglob("*"):

    if not arquivo.is_file():
        continue

    if arquivo.suffix.lower() != ".txt":
        continue

    try:
        texto = arquivo.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    except Exception as erro:
        print(f"Erro ao ler {arquivo}: {erro}")
        continue

    palavras = re.findall(r"\b\w+\b", texto.lower())

    palavras = [
        palavra
        for palavra in palavras
        if palavra not in stopwords
    ]

    contador = Counter(palavras)

    documentos[arquivo] = contador


# -------------------------
# MOSTRAR RESULTADOS
# -------------------------

for arquivo, contador in documentos.items():

    print(f"\nArquivo: {arquivo}")

    print("Palavras mais frequentes:")

    for palavra, quantidade in contador.most_common(10):
        print(f"  {palavra}: {quantidade}")