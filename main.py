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

    def pays(self, bill):
        return bill.amount / 2

class Pdfreport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass

the_bill = Bill(amount=100, period="january 2022")
adi = Flatmate(name="adi", days_in_house = 20)

print(adi.pays(bill= the_bill))

