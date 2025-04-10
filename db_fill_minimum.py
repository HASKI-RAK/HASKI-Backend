import os

import psycopg2

# Establishing the connection
conn = psycopg2.connect(
    database=os.environ.get("DB_NAME", "haski"),
    user="postgres",
    password=os.environ.get("DB_PASSWORD", "postgres"),
    host=os.environ.get("DB_HOST", "127.0.0.1"),
    port=os.environ.get("DB_PORT", 5432),
)

conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Fill Database with example data. Insert the following data into DB:

# Create learning path algorithms
sql = """
    INSERT INTO learning_path_algorithm (short_name, full_name)
    VALUES ('default', 'Default Learning Path Algorithm')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_algorithm (short_name, full_name)
    VALUES ('aco', 'Ant Colony Optimization')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_algorithm (short_name, full_name)
    VALUES ('ga', 'Genetic Algorithm')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_algorithm (short_name, full_name)
    VALUES ('graf', 'Graf et al.')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_algorithm (short_name, full_name)
    VALUES ('tyche', 'Tyche')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_algorithm (short_name, full_name)
    VALUES ('nestor', 'Nestor')
"""
cursor.execute(sql)

conn.commit()
# Closing the connection
conn.close()
