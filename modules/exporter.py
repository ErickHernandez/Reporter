from modules.csv_handler import write_csv
from modules.smtp import SMTP


class Exporter:
    
    def exportToCSV(self, data:list, filename:str):
        write_csv(filename=filename, headers=data[0], rows=data)

    def exportToJSON(self, data:list, filename:str):
        pass

    def exportFileToEmail(self, smtp:SMTP, email_receivers:list, subject:str, body:str, filename:str):
        for email in email_receivers:
            smtp.sendFileByEmail(subject, body, email, filename)