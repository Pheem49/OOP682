from abc import abstractmethod

class Printer:
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan_document(self):
        pass

class Fix:
    @abstractmethod
    def fax_document(self, document):
        pass

class MultiFunctionPrinter(Printer, Scanner, Fix):
    def print_document(self, document):
        print(f"Printing document: {document}")

    def scan_document(self):
        print("Scanning document...")
        return "Scanned Document"

    def fax_document(self, document):
        print(f"Faxing document: {document}")