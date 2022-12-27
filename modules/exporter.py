from modules.csv_handler import write_csv

class Exporter:
    
    def exportToCSV(self, data:list, filename:str):
        write_csv(filename=filename, headers=data[0], rows=data)

    def exportToJSON(self, data:list, filename:str):
        pass

    def exportToEmail(self, data:list, emails:list):
        pass