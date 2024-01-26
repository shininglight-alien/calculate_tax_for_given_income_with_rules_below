# Calculate income tax for the given income by adhering to the rules below

class TaxCalculator:
    def __init__(self, income):
        self.income = income

    def calculate_tax(self):
        if self.income <= 10000:
            return 0
        elif self.income <= 20000:
            return (self.income - 10000) * 0.10
        else:
            return 10000 * 0.10 + (self.income - 20000) * 0.20
    
# test the class
tax_calculator = TaxCalculator(45000)
tax = tax_calculator.calculate_tax()
print(f"The income tax for an income of ${tax_calculator.income} is ${tax}.")