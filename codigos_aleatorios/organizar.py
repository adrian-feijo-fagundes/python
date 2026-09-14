from pathlib import Path
import shutil

input_folder = Path("pasta")
output_folder = Path("resultado")


output_folder.mkdir(exist_ok=True)

for file in input_folder.rglob("*"):
    if file.is_file():
        extension = file.suffix[1:]

        if extension:
            destino = output_folder / extension
            destino.mkdir(exist_ok=True)

            shutil.move(file, destino / file.name)