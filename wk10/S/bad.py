class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate_pdf(self):
        # Placeholder for PDF generation logic
        pdf_report = f"PDF report generated with data: {self.data}"
        return pdf_report
    
    def generate_excel(self):
        # Placeholder for Excel generation logic
        excel_report = f"Excel report generated with data: {self.data}"
        return excel_report
    
    def send_email(self, recipient):
        # Placeholder for email sending logic
        email_status = f"Report sent to {recipient}"
        return email_status
    