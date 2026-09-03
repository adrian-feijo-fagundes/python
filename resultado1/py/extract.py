from pathlib import Path

pasta = Path("arquivos-aleatorios")

extensoes = {}

for arquivo in pasta.iterdir():
    if arquivo.is_file():
        if arquivo.suffix in extensoes:
            extensoes[arquivo.suffix] += 1
        else:
            extensoes[arquivo.suffix] = 1
    else:
        print(arquivo)
        for arquivo2 in pasta.iterdir():
            if arquivo2.is_file():
                if arquivo2.suffix in extensoes:
                    extensoes[arquivo2.suffix] += 1
                else:
                    extensoes[arquivo2.suffix] = 1



output = open("resultado.txt", "w")

for extensao, quantidade in extensoes.items():
    output.write(f"{extensao}: {quantidade}\n")

output.close()


