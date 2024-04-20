"""ezpc_queries.py"""

# CHECK

verify_login_query = "SELECT * FROM user_details WHERE username = %s AND password = %s"

check_username_query = "SELECT * FROM user_details WHERE username = %s"

# INSERT

user_insert_query = "INSERT INTO user_details (user_id, username, password) VALUES (%s, %s, %s)"

part_insert_query = "INSERT INTO parts_details (part_id, part_type, part_brand, part_name, part_price) VALUES (%s, %s, %s, %s, %s)"

# DELETE

user_delete_query = "DELETE FROM user_details WHERE username = %s"