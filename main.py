import webbrowser
import os
from fpdf import FPDF

class Bill:
    """
    object that contains data about the bill

    """
    def __init__(self, amount, period):
        self.period = period
        self.amount = amount

class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays for the bill
    """
    def __init__(self, name: str, days_in_house:int):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return weight * bill.amount

class Pdfreport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        pdf = FPDF(orientation='P', unit= 'pt', format='A4')
        pdf.add_page()

        #Add the icon of house
        pdf.image("house.png", w=30, h=30)

        # Insert Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates bill", border = 0, align='C', ln= 1)

        # Insert period lable and value
        pdf.set_font(family='Times', size=20, style='B')
        pdf.cell(w=90, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt= bill.period, border=0, ln=1)


        #name and due amount of first flatmate
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=90, h=40, txt= flatmate1.name, border=0)   ###I can make border = 1 to have a border
        pdf.cell(w=150, h=40, txt= flatmate1_pay, border=0, ln=1)

        #name and due amount of second flatmate
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=90, h=40, txt= flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt= flatmate2_pay, border=0, ln=1)  ### I can change height to make it look like its below each other

        pdf.output(self.filename)
        #to open the pdf automatically after its generated,
        webbrowser.open('file://'+os.path.realpath(self.filename))


the_bill = Bill(amount=120, period="Feb 2022")
adi = Flatmate(name="adi", days_in_house = 20)
arpita = Flatmate(name="arpita", days_in_house=25)
print("Adi has to pay: ", adi.pays(bill= the_bill, flatmate2 = arpita))
print("Arpita has to pay: ", arpita.pays(bill= the_bill, flatmate2 = adi))

pdf_report = Pdfreport(filename="Report1.pdf")
pdf_report.generate(flatmate1=adi, flatmate2=arpita, bill= the_bill)



