from pandas import read_excel
from glob import glob
from fpdf import FPDF
from pathlib import Path

file_paths = glob('invoices/*xlsx')

for single_file_path in file_paths:
    data_frame = read_excel(single_file_path, sheet_name='Sheet 1')

    pdf = FPDF(orientation='P', unit='mm', format='A4')

    pdf.add_page()

    file_name = Path(single_file_path).stem

    invoice_number, date = file_name.split('-')

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice number. {invoice_number}', ln=1)
    pdf.cell(w=50, h=8, txt=f'Date {date}', ln=1)

    pdf.output(f'PDFs/{file_name}.pdf')

