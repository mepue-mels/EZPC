"""ezpc_queries.py"""

# CHECK

verify_login_query = "SELECT * FROM user_details WHERE username = %s AND password = %s"

check_username_query = "SELECT * FROM user_details WHERE username = %s"

# INSERT

user_insert_query = "INSERT INTO user_details (user_id, username, password) VALUES (%s, %s, %s)"

# DELETE