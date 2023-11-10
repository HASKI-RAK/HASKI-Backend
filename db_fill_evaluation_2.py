import os

import psycopg2

# Establishing the connection
conn = psycopg2.connect(
    database=os.environ.get("DB_NAME", "haski"),
    user="postgres",
    password=os.environ.get("DB_PASSWORD", "genericPassword"),
    host=os.environ.get("DB_HOST", "127.0.0.1"),
    port=os.environ.get("DB_PORT", 5432),
)

conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Team Kempten', 'HS-KE', 2, 'course_creator')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('musterstudent-1', 'HS-KE', 50, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('musterstudent-2', 'HS-KE', 51, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('musterstudent-3', 'HS-KE', 52, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('musterstudent-4', 'HS-KE', 53, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('musterstudent-5', 'HS-KE', 54, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Jan Hendrick Hallwachs', 'HS-KE', 57, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Simon Gapicev', 'HS-KE', 58, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Edem Mustafaev', 'HS-KE', 59, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Emil Geier', 'HS-KE', 60, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Melissa Sieber', 'HS-KE', 61, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Maximilian Mehling', 'HS-KE', 62, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Dennis Berg', 'HS-KE', 63, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Eduard Ganske', 'HS-KE', 64, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Yagmur Baser', 'HS-KE', 65, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Julius Winkeler', 'HS-KE', 66, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Daniel Grubinka', 'HS-KE', 67, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Noah Szymanski', 'HS-KE', 68, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Nick Besler', 'HS-KE', 69, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Nikolas Vollmer', 'HS-KE', 70, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Lukas Berger', 'HS-KE', 71, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Pascal Morawietz', 'HS-KE', 72, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Alexander Dosch', 'HS-KE', 73, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Jan Witkowski', 'HS-KE', 74, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Kilian Ulrich Siffl', 'HS-KE', 75, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Valentin Boddin', 'HS-KE', 76, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Johannes Mayr', 'HS-KE', 77, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('David Böshans', 'HS-KE', 78, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Aron Reichart', 'HS-KE', 79, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Franziska Maul', 'HS-KE', 80, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Ben Erben', 'HS-KE', 81, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Maren Bräckow', 'HS-KE', 82, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Jaqueline Kuhn', 'HS-KE', 83, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Benedikt Adams', 'HS-KE', 84, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Niklas Jan Renneberg', 'HS-KE', 85, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Dorothea Stephanie Mittermaier', 'HS-KE', 86, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Tim Sebastian Fiedler', 'HS-KE', 87, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Christian Claaßen', 'HS-KE', 88, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Aléna Maria Brantzen', 'HS-KE', 89, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Marcel Eisele', 'HS-KE', 90, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Alina Eser', 'HS-KE', 91, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Keno Weber', 'HS-KE', 92, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Eileen Schuster', 'HS-KE', 93, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Daniel Moor', 'HS-KE', 94, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Yannick Bammer', 'HS-KE', 95, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Moritz Rösler', 'HS-KE', 96, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Maximilian Tammer', 'HS-KE', 97, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Markus Leander Rottach', 'HS-KE', 98, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Nuh Ismail Aydin', 'HS-KE', 99, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Michael Riegger', 'HS-KE', 100, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Raphael Enrique Harbich', 'HS-KE', 101, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Alexander Achtmann', 'HS-KE', 102, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Lucas Hauptmann', 'HS-KE', 103, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Hendrik Karsch', 'HS-KE', 104, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Leon Bablick', 'HS-KE', 105, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Joshua Günter', 'HS-KE', 106, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Leon Mros', 'HS-KE', 107, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('John Michael Bieber', 'HS-KE', 108, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Fabian Buchenberg', 'HS-KE', 109, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Jonas Alfons Beck', 'HS-KE', 110, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Daniel Detter', 'HS-KE', 111, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Niklas Schneider', 'HS-KE', 112, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('David Kolk', 'HS-KE', 113, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Tom Niklas', 'HS-KE', 114, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Maximilian Bartz', 'HS-KE', 115, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Christian Lootz', 'HS-KE', 116, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Franziska Melzl', 'HS-KE', 117, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Selma Donlagic', 'HS-KE', 118, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Mika Emilio Angeli', 'HS-KE', 119, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Philipp Schöb', 'HS-KE', 120, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Betül Koytaviloglu', 'HS-KE', 121, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Lukas Wassermann', 'HS-KE', 122, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Paul Gerhard Wittmann', 'HS-KE', 123, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Benjamin Bily', 'HS-KE', 124, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Emilio Albrecht', 'HS-KE', 125, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Jorge Mandlmaier', 'HS-KE', 126, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Franz Felix Gold', 'HS-KE', 127, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Christoph Zengerle', 'HS-KE', 128, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Alisa Knobelspies', 'HS-KE', 129, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Tobias Felder', 'HS-KE', 130, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Felix Walter Gebert', 'HS-KE', 131, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Pasquale Pilz', 'HS-KE', 132, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Deborah Keckeis', 'HS-KE', 133, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Simon Ruepp', 'HS-KE', 134, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Marcelo Santos Neves', 'HS-KE', 135, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Silvan Müller', 'HS-KE', 136, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Julian Alexander Kofler', 'HS-KE', 137, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Nour Alomar', 'HS-KE', 138, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Johann Stang', 'HS-KE', 139, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('David Kapfer', 'HS-KE', 140, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Badr Masharka', 'HS-KE', 141, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Carina Erben', 'HS-KE', 142, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Philipp Samuel Hagel', 'HS-KE', 143, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Anda Podniece', 'HS-KE', 144, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Melissa Storf', 'HS-KE', 145, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Andrei Casian', 'HS-KE', 146, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Thomas Sebastian Ney', 'HS-KE', 147, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Ralf Stockreiter', 'HS-KE', 148, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Martin Elsässer', 'HS-KE', 149, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Anel Dervisic', 'HS-KE', 150, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Jonah Bachmeier', 'HS-KE', 151, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Johannes Stefan Thomas Kersting', 'HS-KE', 152, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Jonas Langbauer', 'HS-KE', 153, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Jakob Steinhauser', 'HS-KE', 154, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Nikolas Jakob Zagora', 'HS-KE', 155, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Thimo Thorandt', 'HS-KE', 156, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Mahnaz Heidarbeiki Mehneh', 'HS-KE', 157, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Jonas Baumgardt', 'HS-KE', 158, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Mahmut Aktas', 'HS-KE', 159, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Lucas Erhard Alfons Gangloff', 'HS-KE', 160, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Selcuk Oruc', 'HS-KE', 161, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Luca Guido Tillinger', 'HS-KE', 162, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Adrian Leandro Ruf', 'HS-KE', 163, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Adrian Leandro Ruf', 'HS-KE', 164, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Anton Gerlitz', 'HS-KE', 165, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Arif Duman', 'HS-KE', 166, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Nathan Senn', 'HS-KE', 167, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Antonio-Gabriel Chacón Menke', 'HS-KE', 168, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course (lms_id, name, university)
    VALUES (6, 'SE - Entwurfsmuster 1', 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course (lms_id, name, university)
    VALUES (5, 'SE - Entwurfsmuster 2', 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_creator (user_id)
    VALUES (1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_creator_course (course_id, course_creator_id, created_at, last_updated)
    VALUES (1, 1, '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_creator_course (course_id, course_creator_id, created_at, last_updated)
    VALUES (2, 1, '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (1, true, 1, true, 'Erste Schritte', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (2, true, 1, true, 'Entwurfsmuster Allgemein', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (3, true, 1, true, 'Feedback zu Entwurfsmuster Allgemein', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (4, true, 1, true, 'Bekannte Entwurfsmuster', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (5, true, 1, true, 'Feedback vor Strategie', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (6, true, 1, true, 'Strategie', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (7, true, 1, true, 'Feedback zu Strategie und Zustand', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (8, true, 1, true, 'Zustand', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (9, true, 1, true, 'Feedback zu Zustand und Adapter', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (10, true, 1, true, 'Adapter', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (11, true, 1, true, 'Feedback zu Adapter und Fassade', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (12, true, 1, true, 'Fassade', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (13, true, 1, true, 'Feedback zu Fassade', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (14, true, 1, true, 'Zwischen-Evaluation am Ende von Entwurfsmuster 1', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (15, true, 1, true, 'Feedback vor Decorator', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (16, true, 1, true, 'Decorator', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (17, true, 1, true, 'Feedback zu Decorator und Command', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (18, true, 1, true, 'Command', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (19, true, 1, true, 'Feedback zu Command', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (20, true, 1, true, 'Money', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (21, true, 1, true, 'Feedback vor Builder', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (22, true, 1, true, 'Builder', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (23, true, 1, true, 'Feedback zu Builder', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, university, created_by, created_at, last_updated)
    VALUES (24, true, 1, true, 'Letzte Schritte', 'HS-KE', 'Dimitri Bigler', '2023-11-09 10:00:00', '2023-11-09 10:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 6)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 7)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 8)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 9)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 10)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 11)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 12)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 13)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (1, 14)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 15)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 16)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 17)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 18)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 19)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 20)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 21)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 22)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 23)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 24)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (405, 'feedback', 'RQ', 'Begriffserklärung HASKI', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (406, 'h5pactivity', 'ÜB', 'Intuitive Reihenfolge der Lernelemente', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (407, 'feedback', 'RQ', 'Evaluation vor dem Thema "Entwurfsmuster Allgemein"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (408, 'h5pactivity', 'KÜ', 'Kurzübersicht - EM Allg.', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (409, 'resource', 'EK', 'Erklärung - EM Allg.', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (410, 'resource', 'AN', 'Animation - EM Allg.', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (411, 'h5pactivity', 'BE', 'Beispiel - EM Allg.', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (412, 'h5pactivity', 'SE', 'Selbsteinschätzungstest - EM Allg.', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (413, 'h5pactivity', 'ÜB', 'Leichte Übung - 1 - EM Allg.', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (414, 'h5pactivity', 'ÜB', 'Leichte Übung - 2 - EM Allg.', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (415, 'h5pactivity', 'ÜB', 'Mittlere Übung - 1 - EM Allg.', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (416, 'h5pactivity', 'ÜB', 'Mittlere Übung - 2 - EM Allg.', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (417, 'h5pactivity', 'ÜB', 'Schwere Übung - 1 - EM Allg.', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (418, 'h5pactivity', 'ÜB', 'Schwere Übung - 2 - EM Allg.', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (419, 'h5pactivity', 'ZF', 'Zusammenfassung - EM Allg.', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (420, 'h5pactivity', 'ZL', 'Zusatzliteratur - EM Allg.', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (421, 'feedback', 'RQ', 'Evaluation nach dem Thema "Entwurfsmuster Allgemein"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (422, 'resource', 'EK', 'Erklärung - Bekannte EM', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (423, 'feedback', 'RQ', 'Evaluation vor dem Thema "Strategie"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (424, 'h5pactivity', 'KÜ', 'Kurzübersicht - Strategie', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 10:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (425, 'resource', 'EK', 'Erklärung - Strategie', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (426, 'resource', 'AN', 'Animation - Strategie', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (427, 'h5pactivity', 'BE', 'Beispiel - Strategie', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (428, 'h5pactivity', 'SE', 'Selbsteinschätzungstest - Strategie', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (429, 'h5pactivity', 'ÜB', 'Leichte Übung - 1 - Strategie', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (430, 'h5pactivity', 'ÜB', 'Leichte Übung - 2 - Strategie', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (431, 'h5pactivity', 'ÜB', 'Mittlere Übung - 1 - Strategie', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (432, 'h5pactivity', 'ÜB', 'Mittlere Übung - 2 - Strategie', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (433, 'h5pactivity', 'ÜB', 'Schwere Übung - 1 - Strategie', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (434, 'h5pactivity', 'ÜB', 'Schwere Übung - 2 - Strategie', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (435, 'h5pactivity', 'ZF', 'Zusammenfassung - Strategie', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (436, 'h5pactivity', 'ZL', 'Zusatzliteratur - Strategie', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (437, 'feedback', 'RQ', 'Evaluation nach dem Thema "Strategie"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (438, 'feedback', 'RQ', 'Evaluation vor dem Thema "Zustand"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (439, 'h5pactivity', 'KÜ', 'Kurzübersicht - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (440, 'resource', 'EK', 'Erklärung - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (441, 'resource', 'AN', 'Animation - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (442, 'h5pactivity', 'BE', 'Beispiel - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (443, 'h5pactivity', 'SE', 'Selbsteinschätzungstest - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (444, 'h5pactivity', 'ÜB', 'Leichte Übung - 1 - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (445, 'h5pactivity', 'ÜB', 'Leichte Übung - 2 - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (446, 'h5pactivity', 'ÜB', 'Mittlere Übung - 1 - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (447, 'h5pactivity', 'ÜB', 'Mittlere Übung - 2 - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (448, 'h5pactivity', 'ÜB', 'Mittlere Übung - 2 - Zustand - Lösung', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (449, 'h5pactivity', 'ÜB', 'Schwere Übung - 1 - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (450, 'h5pactivity', 'ÜB', 'Schwere Übung - 1 Aufgabe 1 Heatmap - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (451, 'h5pactivity', 'ÜB', 'Schwere Übung - 1 Aufgabe 1 - Zustand - Lösung', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (452, 'h5pactivity', 'ÜB', 'Schwere Übung - 1 Aufgabe 2 Heatmap - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (453, 'h5pactivity', 'ÜB', 'Schwere Übung - 2 - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (454, 'h5pactivity', 'ZF', 'Zusammenfassung - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (455, 'h5pactivity', 'ZL', 'Zusatzliteratur - Zustand', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 11:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (456, 'feedback', 'RQ', 'Evaluation nach dem Thema "Zustand"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (457, 'feedback', 'RQ', 'Evaluation vor dem Thema "Adapter"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (458, 'h5pactivity', 'KÜ', 'Kurzübersicht - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (459, 'resource', 'EK', 'Erklärung - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (460, 'resource', 'AN', 'Animation - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (461, 'h5pactivity', 'BE', 'Beispiel - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (462, 'h5pactivity', 'SE', 'Selbsteinschätzungstest - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (463, 'h5pactivity', 'ÜB', 'Leichte Übung - 1 - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (464, 'h5pactivity', 'ÜB', 'Leichte Übung - 2 - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (465, 'h5pactivity', 'ÜB', 'Mittlere Übung - 1 - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (466, 'h5pactivity', 'ÜB', 'Mittlere Übung - 2 - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (467, 'h5pactivity', 'ÜB', 'Schwere Übung - 1 - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (468, 'h5pactivity', 'ÜB', 'Schwere Übung - 2 - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (469, 'h5pactivity', 'ÜB', 'Schwere Übung - 3 - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (470, 'h5pactivity', 'ZF', 'Zusammenfassung - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (471, 'h5pactivity', 'ZL', 'Zusatzliteratur - Adapter', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (472, 'feedback', 'RQ', 'Evaluation nach dem Thema "Adapter"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (473, 'feedback', 'RQ', 'Evaluation vor dem Thema "Fassade"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (474, 'h5pactivity', 'KÜ', 'Kurzübersicht - Fassade', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (475, 'resource', 'EK', 'Erklärung - Fassade', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (476, 'resource', 'AN', 'Animation - Fassade', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (477, 'h5pactivity', 'BE', 'Beispiel - Fassade', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (478, 'h5pactivity', 'SE', 'Selbsteinschätzungstest - Fassade', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (479, 'h5pactivity', 'ÜB', 'Leichte Übung - 1 - Fassade', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (480, 'h5pactivity', 'ÜB', 'Leichte Übung - 2 - Fassade', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (481, 'h5pactivity', 'ÜB', 'Mittlere Übung - 1 - Fassade', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (482, 'h5pactivity', 'ÜB', 'Mittlere Übung - 2 - Fassade', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (483, 'h5pactivity', 'ÜB', 'Schwere Übung - 1 - Fassade', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (484, 'h5pactivity', 'ÜB', 'Schwere Übung - 2 - Fassade', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (485, 'h5pactivity', 'ZF', 'Zusammenfassung - Fassade', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (486, 'h5pactivity', 'ZL', 'Zusatzliteratur - Fassade', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (487, 'feedback', 'RQ', 'Evaluation nach dem Thema "Fassade"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (488, 'h5pactivity', 'RQ', 'Evaluation der Themen (EM1)', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (489, 'h5pactivity', 'RQ', 'Retrospektive Reihenfolge der Lernelemente (EM1)', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (490, 'feedback', 'RQ', 'Bewertung von Lernelementen (EM1)', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 12:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (502, 'feedback', 'RQ', 'Evaluation vor dem Thema "Decorator"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (352, 'h5pactivity', 'KÜ', 'Kurzübersicht - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (354, 'resource', 'EK', 'Erklärung - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (393, 'resource', 'AN', 'Animation - Funktionserweiterung - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (392, 'resource', 'AN', 'Animation - Klassenexplosion - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (344, 'h5pactivity', 'BE', 'Beispiel - Funktionserweiterung - C++ - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (346, 'h5pactivity', 'BE', 'Beispiel - Klassenexplosion - C++- Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (349, 'h5pactivity', 'SE', 'Selbsteinschätzungstest - Funktionserweiterung - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (351, 'h5pactivity', 'SE', 'Selbsteinschätzungstest - Klassenexplosion - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (355, 'h5pactivity', 'ÜB', 'Leichte Übung - 1 - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (356, 'h5pactivity', 'ÜB', 'Leichte Übung - 2 - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (357, 'h5pactivity', 'ÜB', 'Mittlere Übung - 1 - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (358, 'h5pactivity', 'ÜB', 'Mittlere Übung - 2 - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (359, 'h5pactivity', 'ÜB', 'Schwere Übung - 1 - C++ - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (360, 'h5pactivity', 'ÜB', 'Schwere Übung - 2 - C++ - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (343, 'h5pactivity', 'ZF', 'Zusammenfassung - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (353, 'h5pactivity', 'ZL', 'Zusatzliteratur - Decorator', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (503, 'feedback', 'RQ', 'Evaluation nach dem Thema "Decorator"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (504, 'feedback', 'RQ', 'Evaluation vor dem Thema "Command"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (361, 'h5pactivity', 'KÜ', 'Kurzübersicht - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (362, 'resource', 'EK', 'Erklärung - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (394, 'resource', 'AN', 'Animation - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (363, 'h5pactivity', 'BE', 'Beispiel - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (367, 'h5pactivity', 'SE', 'Selbsteinschätzungstest - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (369, 'h5pactivity', 'ÜB', 'Leichte Übung - 1 - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (370, 'h5pactivity', 'ÜB', 'Leichte Übung - 2 - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (371, 'h5pactivity', 'ÜB', 'Mittlere Übung - 1 - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (372, 'h5pactivity', 'ÜB', 'Mittlere Übung - 2 - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (395, 'h5pactivity', 'ÜB', 'Mittlere Übung - 3 - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (373, 'h5pactivity', 'ÜB', 'Schwere Übung - 1 - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (374, 'h5pactivity', 'ÜB', 'Schwere Übung - 2 - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (375, 'h5pactivity', 'ZF', 'Zusammenfassung - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (376, 'h5pactivity', 'ZL', 'Zusatzliteratur - Command', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (505, 'feedback', 'RQ', 'Evaluation nach dem Thema "Command"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (377, 'resource', 'EK', 'Erklärung - Money', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (506, 'feedback', 'RQ', 'Evaluation vor dem Thema "Builder"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (378, 'h5pactivity', 'KÜ', 'Kurzübersicht - Builder', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (379, 'resource', 'EK', 'Erklärung - Builder', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (396, 'resource', 'AN', 'Animation - Builder', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (380, 'h5pactivity', 'BE', 'Beispiel - C++ - Builder', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (381, 'h5pactivity', 'SE', 'Selbsteinschätzungstest - Builder', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (382, 'h5pactivity', 'ÜB', 'Leichte Übung - 1 - Builder', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (383, 'h5pactivity', 'ÜB', 'Leichte Übung - 2 - Builder', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (384, 'h5pactivity', 'ÜB', 'Mittlere Übung - 1 - C++ - Builder', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (385, 'h5pactivity', 'ÜB', 'Mittlere Übung - 2 - Builder', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (386, 'h5pactivity', 'ÜB', 'Schwere Übung - 1 - C++ - Builder', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (387, 'h5pactivity', 'ÜB', 'Schwere Übung - 2 - C++ - Builder', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (388, 'h5pactivity', 'ZF', 'Zusammenfassung - Builder', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (389, 'h5pactivity', 'ZL', 'Zusatzliteratur - Builder', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (507, 'feedback', 'RQ', 'Evaluation nach dem Thema "Builder"', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (512, 'h5pactivity', 'RQ', 'Evaluation der Themen (EM2)', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (509, 'h5pactivity', 'RQ', 'Retrospektive Reihenfolge der Lernelemente (EM2)', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (508, 'feedback', 'RQ', 'Bewertung von Lernelementen (EM2)', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (510, 'feedback', 'RQ', 'Abschluss-Evaluation', 'HS-KE', 'Gesine Wagner',\
    '2023-11-09 13:30:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (1, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (1, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (1, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 6)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 7)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 8)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 9)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 10)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 11)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 12)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 13)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 14)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 15)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 16)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (3, 17)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (4, 18)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (5, 19)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 20)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 21)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 22)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 23)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 24)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 25)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 26)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 27)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 28)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 29)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 30)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 31)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 32)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (7, 33)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (7, 34)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 35)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 36)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 37)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 38)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 39)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 40)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 41)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 42)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 43)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 44)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 45)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 46)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 47)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 48)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 49)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 50)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (8, 51)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (9, 52)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (9, 53)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 54)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 55)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 56)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 57)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 58)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 59)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 60)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 61)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 62)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 63)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 64)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 65)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 66)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (10, 67)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (11, 68)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (11, 69)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (12, 70)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (12, 71)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (12, 72)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (12, 73)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (12, 74)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (12, 75)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (12, 76)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (12, 77)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (12, 78)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (12, 79)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (12, 80)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (12, 81)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (12, 82)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (13, 83)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (14, 84)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (14, 85)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (14, 86)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (15, 87)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 88)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 89)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 90)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 91)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 92)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 93)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 94)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 95)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 96)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 97)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 98)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 99)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 100)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 101)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 102)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (16, 103)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (17, 104)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (17, 105)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 106)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 107)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 108)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 109)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 110)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 111)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 112)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 113)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 114)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 115)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 116)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 117)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 118)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (18, 119)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (19, 120)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (21, 121)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (22, 122)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (23, 123)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (23, 124)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (23, 125)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (23, 126)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (23, 127)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (23, 128)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (23, 129)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (23, 130)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (23, 131)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (23, 132)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (23, 133)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (23, 134)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (23, 135)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (24, 136)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (24, 137)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (24, 138)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (24, 139)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (24, 140)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    
    VALUES (3)
    """
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (6)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (7)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (8)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (9)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (10)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (11)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (12)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (13)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (14)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (15)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (16)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (17)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (18)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (19)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (20)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (21)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (22)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (23)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (24)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (25)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (26)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (27)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (28)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (29)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (30)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (31)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (32)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (33)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (34)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (35)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (36)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (37)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (38)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (39)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (40)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (41)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (42)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (43)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (44)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (45)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (46)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (47)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (48)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (49)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (50)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (51)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (52)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (53)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (54)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (55)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (56)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (57)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (58)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (59)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (60)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (61)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (62)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (63)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (64)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (65)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (66)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (67)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (68)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (69)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (70)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (71)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (72)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (73)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (74)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (75)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (76)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (77)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (78)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (79)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (80)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (81)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (82)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (83)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (84)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (85)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (86)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (87)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (88)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (89)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (90)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (91)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (92)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (93)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (94)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (95)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (96)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (97)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (98)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (99)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (100)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (101)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (102)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (103)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (104)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (105)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (106)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (107)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (108)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (109)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (110)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (111)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (112)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (113)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (114)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (115)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (116)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (117)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (118)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (1, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (2, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (3, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (4, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (5, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (6, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (7, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (8, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (9, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (10, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (11, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (12, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (13, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (14, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (15, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (16, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (17, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (18, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (19, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (20, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (21, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (22, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (23, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (24, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (25, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (26, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (27, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (28, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (29, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (30, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (31, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (32, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (33, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (34, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (35, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (36, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (37, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (38, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (39, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (40, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (41, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (42, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (43, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (44, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (45, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (46, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (47, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (48, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (49, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (50, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (51, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (52, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (53, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (54, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (55, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (56, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (57, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (58, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (59, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (60, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (61, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (62, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (63, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (64, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (65, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (66, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (67, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (68, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (69, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (70, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (71, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (72, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (73, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (74, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (75, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (76, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (77, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (78, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (79, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (80, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (81, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (82, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (83, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (84, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (85, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (86, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (87, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (88, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (89, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (90, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (91, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (92, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (93, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (94, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (95, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (96, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (97, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (98, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (99, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (100, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (101, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (102, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (103, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (104, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (105, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (106, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (107, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (108, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (109, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (110, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (111, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (112, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (113, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (114, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (115, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (116, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (117, 1, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (1, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (2, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (3, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (4, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (5, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (6, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (7, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (8, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (9, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (10, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (11, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (12, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (13, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (14, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (15, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (16, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (17, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (18, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (19, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (20, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (21, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (22, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (23, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (24, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (25, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (26, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (27, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (28, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (29, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (30, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (31, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (32, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (33, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (34, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (35, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (36, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (37, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (38, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (39, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (40, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (41, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (42, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (43, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (44, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (45, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (46, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (47, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (48, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (49, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (50, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (51, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (52, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (53, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (54, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (55, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (56, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (57, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (58, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (59, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (60, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (61, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (62, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (63, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (64, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (65, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (66, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (67, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (68, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (69, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (70, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (71, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (72, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (73, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (74, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (75, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (76, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (77, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (78, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (79, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (80, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (81, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (82, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (83, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (84, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (85, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (86, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (87, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (88, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (89, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (90, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (91, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (92, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (93, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (94, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (95, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (96, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (97, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (98, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (99, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (100, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (101, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (102, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (103, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (104, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (105, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (106, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (107, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (108, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (109, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (110, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (111, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (112, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (113, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (114, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (115, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (116, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course(student_id, course_id, perception_dimension, perception_value, input_dimension, input_value, processing_dimension, processing_value, understanding_dimension, understanding_value)
    VALUES (117, 2, 'ref', 0, 'int', 0, 'vrb', 0, 'seq', 0)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(1, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(2, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(3, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(4, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(5, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(6, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(7, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(8, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(9, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(10, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(11, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(12, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(13, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(14, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(15, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(16, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(17, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(18, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(19, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(20, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(21, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(22, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(23, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(24, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(25, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(26, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(27, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(28, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(29, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(30, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(31, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(32, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(33, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(34, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(35, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(36, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(37, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(38, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(39, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(40, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(41, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(42, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(43, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(44, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(45, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(46, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(47, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(48, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(49, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(50, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(51, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(52, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(53, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(54, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(55, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(56, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(57, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(58, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(59, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(60, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(61, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(62, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(63, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(64, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(65, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(66, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(67, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(68, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(69, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(70, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(71, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(72, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(73, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(74, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(75, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(76, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(77, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(78, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(79, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(80, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(81, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(82, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(83, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(84, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(85, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(86, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(87, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(88, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(89, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(90, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(91, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(92, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(93, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(94, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(95, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(96, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(97, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(98, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(99, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(100, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(101, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(102, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(103, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(104, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(105, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(106, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(107, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(108, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(109, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(110, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(111, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(112, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(113, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(114, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(115, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(116, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 1, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 2, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 3, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 4, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 5, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 6, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 7, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 8, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 9, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 10, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 11, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 12, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 13, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 14, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 15, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 16, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 17, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 18, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 19, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 20, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 21, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 22, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 23, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic(student_id, topic_id, done, done_at)
    VALUES(117, 24, false, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(1, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(2, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(3, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(4, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(5, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(6, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(7, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(8, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(9, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(10, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(11, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(12, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(13, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(14, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(15, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(16, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(17, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(18, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(19, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(20, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(21, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(22, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(23, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(24, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(25, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(26, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(27, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(28, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(29, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(30, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(31, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(32, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(33, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(34, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(35, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(36, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(37, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(38, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(39, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(40, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(41, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(42, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(43, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(44, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(45, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(46, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(47, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(48, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(49, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(50, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(51, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(52, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(53, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(54, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(55, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(56, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(57, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(58, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(59, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(60, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(61, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(62, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(63, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(64, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(65, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(66, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(67, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(68, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(69, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(70, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(71, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(72, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(73, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(74, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(75, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(76, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(77, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(78, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(79, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(80, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(81, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(82, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(83, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(84, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(85, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(86, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(87, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(88, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(89, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(90, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(91, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(92, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(93, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(94, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(95, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(96, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(97, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(98, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(99, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(100, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(101, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(102, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(103, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(104, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(105, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(106, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(107, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(108, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(109, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(110, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(111, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(112, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(113, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(114, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(115, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(116, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 1, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 3, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 4, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 5, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 7, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 8, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 9, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 11, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 13, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 14, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 15, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 17, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 18, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 19, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 20, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 21, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 23, '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path(student_id, course_id, based_on, topic_id, calculated_on)
    VALUES(117, 1, 'Jim Haug', 24, '2023-07-20 20:00:00')
"""
cursor.execute(sql)



conn.commit()
# Closing the connection
conn.close()
