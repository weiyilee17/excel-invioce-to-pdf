from pandas import read_excel
from glob import glob
from fpdf import FPDF
from pathlib import Path

file_paths = glob('invoices/*.xlsx')

for single_file_path in file_paths:

    pdf = FPDF(orientation='P', unit='mm', format='A4')

    pdf.add_page()

    file_name = Path(single_file_path).stem

    invoice_number, date = file_name.split('-')

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice number. {invoice_number}', ln=1)
    pdf.cell(w=50, h=8, txt=f'Date: {date}', ln=1)

    data_frame = read_excel(single_file_path, sheet_name='Sheet 1')

    # Add header
    display_columns = [single_column.replace('_', ' ').title() for single_column in data_frame.columns]

    pdf.set_font(family='Times', size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=display_columns[0], border=1)
    pdf.cell(w=70, h=8, txt=display_columns[1], border=1)
    pdf.cell(w=30, h=8, txt=display_columns[2], border=1)
    pdf.cell(w=30, h=8, txt=display_columns[3], border=1)
    pdf.cell(w=30, h=8, txt=display_columns[4], border=1, ln=1)

    # Add rows to the table
    for index, row in data_frame.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=70, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)

    # Add 1 row for total
    total_sum = data_frame['total_price'].sum()

    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=70, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # Show total price summary and logo
    pdf.set_font(family='Times', size=10, style='B')
    pdf.cell(w=30, h=8, txt=f'The total price is {total_sum}', ln=1)

    pdf.set_font(family='Times', size=14, style='B')
    pdf.cell(w=25, h=8, txt='PythonHow')
    pdf.image('pythonhow.png', w=10)

    pdf.output(f'PDFs/{file_name}.pdf')
