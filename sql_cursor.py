import os.path, sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "ezpc.db")
DB = db_path

connection = sqlite3.connect(DB)
cursor = connection.cursor()
cursor.execute("DELETE FROM user_details WHERE user_id = 0;")
connection.commit()
print("Success.")