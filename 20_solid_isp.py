# Scenario: A printer device should implement only the features it supports.
class Printable:
    def print_document(self, document):
        print("Printing:", document)

class Scannable:
    def scan_document(self):
        print("Scanning document")

class BasicPrinter(Printable):
    pass

class MultiFunctionPrinter(Printable, Scannable):
    pass

BasicPrinter().print_document("Assignment.pdf")
device = MultiFunctionPrinter()
device.print_document("Report.pdf")
device.scan_document()
