import pypandoc
from pathlib import Path

current_folder = Path(__file__).resolve().parent.parent.parent / "GitExtra"

markdown_files = list(current_folder.rglob("*.md"))

# print(markdown_files)


input = markdown_files
output = current_folder / "GitUitleg.pdf"

pypandoc.convert_file(input, 'pdf', outputfile=output,
                      extra_args=[
                          # '-V', 'documentclass=extarticle',
                          '-V', 'geometry:margin=2cm',
                          '-V', 'fontsize=12pt',
                          '-V', 'mainfont=Arial',
                          '--pdf-engine=xelatex',
                          '-H', 'float_fix.tex'
                      ])

print(f"done converting {output}")
