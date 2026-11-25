# Scenario: An invoice app separates invoice calculation from printing.
class Invoice:
    def __init__(self, items):
        self.items = items

    def total(self):
        return sum(price * quantity for price, quantity in self.items)

class InvoicePrinter:
    def print_invoice(self, invoice):
        print("Invoice total: Rs.", invoice.total())

invoice = Invoice([(100, 2), (250, 1)])
InvoicePrinter().print_invoice(invoice)
