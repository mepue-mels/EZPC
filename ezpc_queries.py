"""ezpc_queries.py"""

# DISPLAY

display_main_menu = """
---EZPC MENU---
[-1] DELETE
[0] SAVE/EXIT   
[1] SAVED BUILDS
Select option: """

# SELECT

verify_login_query = """
SELECT * FROM user_details 
WHERE username = %s AND password = %s
"""

user_select_username_query = """
SELECT * FROM user_details 
WHERE username = %s
"""

pc_select_query = """
SELECT pc_id AS pc_id, pc_name, case_id, cooler_id, cpu_id, gpu_id, mobo_id, psu_id, ram_id, storage_id
FROM pc_details
WHERE user_id = %s;
"""

part_select_case_query = """
SELECT * FROM case_data
WHERE id = %s
"""

part_select_cooler_query = """
SELECT * FROM cooler_data
WHERE id = %s
"""

part_select_cpu_query = """
SELECT * FROM cpu_data
WHERE id = %s
"""

part_select_gpu_query = """
SELECT * FROM gpu_data
WHERE id = %s
"""

part_select_mobo_query = """
SELECT * FROM mobo_data
WHERE id = %s
"""

part_select_psu_query = """
SELECT * FROM psu_data
WHERE id = %s
"""

part_select_ram_query = """
SELECT * FROM ram_data
WHERE id = %s
"""

part_select_storage_query = """
SELECT * FROM storage_data
WHERE id = %s
"""

part_select_query_list = [part_select_case_query,
                          part_select_cooler_query,
                          part_select_cpu_query,
                          part_select_gpu_query,
                          part_select_mobo_query,
                          part_select_psu_query,
                          part_select_ram_query,
                          part_select_storage_query]

# INSERT

user_insert_query = """
INSERT INTO user_details (user_id, username, password) 
VALUES (%s, %s, %s)
"""

pc_insert_query = """
INSERT INTO pc_details (user_id, pc_name,
case_id, cooler_id, cpu_id, gpu_id, 
mobo_id, psu_id, ram_id, storage_id)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

part_insert_query = "INSERT INTO parts_details (part_id, part_type, part_brand, part_name, part_price) VALUES (%s, %s, %s, %s, %s)"

# UPDATE

pc_update_query = """
UPDATE pc_details
SET case_id = %s, cooler_id = %s, 
cpu_id = %s, gpu_id = %s, 
mobo_id = %s, psu_id = %s, 
ram_id = %s, storage_id = %s
WHERE pc_id = %s;
"""

# DELETE

user_delete_query = "DELETE FROM user_details WHERE username = %s"

pc_delete_query = "DELETE FROM pc_details WHERE pc_id = %s"