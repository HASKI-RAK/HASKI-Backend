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

# Create default learning path for HS-KE
sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('KÜ', 1, true, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('EK', 2, true, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('AN', 3, true, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('SE', 4, true, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('BE', 5, true, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('ÜB', 6, true, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('ZF', 7, true, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('ZL', 8, true, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('RQ', 9, true, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('FO', 10, true, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('LZ', 11, true, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('AB', 12, true,'HS-KE')
"""
cursor.execute(sql)

# Create default learning path for TH-AB
sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('KÜ', 1, true, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('ZL', 2, true, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('EK', 3, true, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('AN', 4, true, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('BE', 5, true, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('SE', 6, true, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('AB', 7, true, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('ÜB', 8, true, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('LZ', 9, true, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('ZF', 10, true, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('RQ', 11, true, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, disabled, university)
    VALUES ('FO', 12, true, 'TH-AB')
"""
cursor.execute(sql)


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
