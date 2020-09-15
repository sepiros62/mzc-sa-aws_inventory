import csv
from fpdf import FPDF

with open('test2.csv', newline='') as f:
        reader = csv.reader(f)
#       pdf = FPDF(orientation = 'L', unit = 'mm', format='A3')
        pdf = FPDF('L','mm', (200, 500))
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin

        pdf.set_font('Times','B',20.0)
        pdf.cell(page_width, 0.0, 'AWS Resource Data', align='C')
        pdf.ln(10)

        pdf.set_font('Courier', '', 10)
        pdf.set_fill_color(153, 153, 153)

        col_width = page_width/8

        pdf.ln(1)

        th = pdf.font_size

        for row in reader:
        #print(row)
                pdf.cell(col_width, th, str(row[0]), fill = True, border=1)
                pdf.cell(col_width, th, row[1], border=1)
                pdf.cell(col_width, th, row[2], fill = True, border=1)
                pdf.cell(col_width, th, row[3], border=1)
                pdf.cell(col_width, th, row[4], fill = True, border=1)
                pdf.cell(col_width, th, row[5], border=1)
                pdf.cell(col_width, th, row[6], fill = True, border=1)
                pdf.cell(col_width, th, row[7], border=1)
                pdf.ln(th)

        pdf.ln(10)

        pdf.set_font('Times','',14.0)
        pdf.cell(page_width, 0.0, '- end of report -', align='C')

        pdf.output('test.pdf', 'F')
[root@awx-server ~]#
