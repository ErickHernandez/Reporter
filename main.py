from modules.db import DB
from modules.smtp import SMTP
from modules.file_handler import read_text_file
from modules.exporter import Exporter

db = DB("127.0.0.1", "dbuser", "dbpass", "dbname", 3306)
conn = db.create_db_connection()

my_query = read_text_file("./queries/employees_by_salary.sql")

result = db.select(conn, my_query)

# Example exporting a compressed csv file by email.

exporter = Exporter()
exporter.exportToCSV(result, "./query_output/myfile.csv")

smtp = SMTP("your.email@gmail.com", "xxxzzzyyyxxx", "smtp.gmail.com", 465)
exporter.exportFileToEmail(
    smtp,
    ["to.email@example.com"],
    "Weekly Report",
    "Hi, report attached!",
    "./query_output/myfile.csv",
)
