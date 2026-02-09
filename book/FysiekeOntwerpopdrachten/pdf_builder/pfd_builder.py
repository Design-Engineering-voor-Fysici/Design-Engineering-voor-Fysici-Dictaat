import pypandoc
from pathlib import Path

current_folder = Path(__file__).resolve().parent
opdrachten_folders = current_folder.parent

markdown_files = list(opdrachten_folders.rglob("*.md"))

for md in markdown_files:
    input = Path(md)
    output = input.with_suffix('.pdf')

    pypandoc.convert_file(input, 'pdf', outputfile=output,
                          extra_args=[
                              '-V', 'geometry:margin=2cm',
                              '-V', 'font-size=16pt',
                              '-V', 'mainfont=Arial'
                          ])

    print(f"done converting {output}")
