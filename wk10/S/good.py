class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self):
        pass

class ExcelReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self):
            # Placeholder for Excel generation logic
        excel_report = f"Excel report generated with data: {self.data}"
        return excel_report
        
class PDFReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self):
            # Placeholder for PDF generation logic
        pdf_report = f"PDF report generated with data: {self.data}"
        return pdf_report
        
class EmailSender:
    def __init__(self, recipient):
        self.recipient = recipient

    def send(self):
            # Placeholder for email sending logic
        email_status = f"Report sent to {self.recipient}"
        return email_status
    
    