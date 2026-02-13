class machine:
    def print_status(self):
        pass
    def scan(self):
        pass
    def fax(self):
        pass

class OldFashionedPrinter(machine):
    def print_status(self):
        super().print_status()
    def scan(self):
        raise NotImplementedError("This printer cannot scan.")
    def fax(self):
        raise NotImplementedError("This printer cannot fax.")
