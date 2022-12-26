from modules.DB import DB
from modules.file_handler import read_text_file

db = DB('127.0.0.1', 'dbuser', 'dbpass', 'dbname', 3306)
conn = db.create_db_connection()

my_query = read_text_file('./queries/employees_by_salary.sql')

result = db.select(conn, my_query)

print(result)