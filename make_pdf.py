from fpdf import FPDF
from datetime import date


class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Times new Romen', 'B', 17)
        # Move to the right
        self.cell(0, 10, 'Shree Raj Marble', border=False, align='L')
        self.line(10, 20, 100, 20)
        self.set_font('Arial', style='B', size=10)
        self.ln(10)
        self.cell(0, 10, 'Subhas park,Plot No. 17, Ranjeet sagar road, Jamnagar Gujarat', border=False, align='L')
        self.ln(5)
        self.cell(0, 10, "GST No : "+str(), border=False, align='L')
        self.ln(5)
        self.cell(0, 10, "Mo No : 1234567890", border=False, align='L')
        self.ln(10)
        self.cell(0, 10, "Invoice Number: 123456", border=False, align='R')
        self.ln(5)
        self.cell(0, 10, "Customer Name: Meet Kumar", border=False, align='R')
        self.ln(5)
        self.cell(0, 10, "Contact Number: 14567890", border=False, align='R')
        self.ln(5)
        self.cell(0, 10, "Date: "+str(date.today()), border=False, align='R')
        self.ln(10)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def bill_titles(self):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(201, 221, 235)
        # Title
        self.cell(20, 6, 'Sr No', 0, 0, 'L', 1)
        self.cell(40, 6, 'Product Name', 0, 0, 'L', 1)
        self.cell(20, 6, 'Quantity', 0, 0, 'L', 1)
        self.cell(40, 6, 'Rate', 0, 0, 'L', 1)
        self.cell(30, 6, 'Tax', 0, 0, 'L', 1)
        self.cell(40, 6, 'Total', 0, 0, 'L', 1)
        # Line break
        self.ln(10)

    def add_products(self, list_products):
        i = 1
        for product in list_products:
            self.cell(20, 6, str(i), 0, 0, 'L')
            self.cell(40, 6, product[0], 0, 0, 'L')
            self.cell(20, 6, product[1], 0, 0, 'L')
            self.cell(40, 6, str(product[2]), 0, 0, 'L')
            self.cell(30, 6, str(product[3]), 0, 0, 'L')
            self.cell(41, 6, str(product[4]), 0, 0, 'L')
            self.ln(5)
            self.line(10, 20, 200, 20)
            i += 1


# pdf = PDF(format='A4', unit='mm')
# pdf.alias_nb_pages()
# pdf.add_page()
# pdf.set_font('Times', '', 12)
# pdf.bill_titles()
# pdf.add_products([('u', '4', 2.0, 1.0, 2.0), ('u', '4', 2.0, 2.0, 4.0), ('u', '4', 2.0, 3.0, 6.0)])
#
# pdf.output('tuto2.pdf', 'F')




 self.cell(w=75,h=7,txt="Shree Raj marble, \nPlot No. 16, Ranjit sagar road, \nJamnagar Gujarat, India",border=1,align='L')
        self.cell(w=75, h=7,txt=str(customer_name.get()) + "\n" + str(add_line1.get()) + "\n" + str(add_line2.get()),border=1, align='L')

        self.ln(10)

        self.cell(70, 7, "GST No : " + str(cus_gst_no.get()), border=1, align='R')

