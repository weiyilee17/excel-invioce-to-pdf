from glob import glob
from fpdf import FPDF
from pathlib import Path

file_paths = glob('text_files/*.txt')

pdf = FPDF(orientation='P', unit='mm', format='A4')

for single_file_path in file_paths:
    file_name = Path(single_file_path).stem

    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=0, h=16, txt=file_name.capitalize(), ln=1)

    with open(single_file_path, 'r') as file:
        content = file.read()

        pdf.set_font(family='Times', style='B', size=12)
        pdf.multi_cell(w=0, h=6, txt=content)

pdf.output('compacted.pdf')
