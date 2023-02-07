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


the_bill = Bill(amount=120, period="january 2022")
adi = Flatmate(name="adi", days_in_house = 20)
arpita = Flatmate(name="arpita", days_in_house=25)
print("Adi has to pay: ", adi.pays(bill= the_bill, flatmate2 = arpita))
print("Arpita has to pay: ", arpita.pays(bill= the_bill, flatmate2 = adi))


