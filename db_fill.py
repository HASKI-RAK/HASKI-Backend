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

# Create admin user
sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Dimitri Bigler', 'HS-KE', 1, 'admin')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (1, 'light', 'admin')
"""
cursor.execute(sql)

sql = """
    INSERT INTO admin (user_id)
    VALUES (1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('David Fischer', 'HS-KE', 2, 'admin')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (2, 'dark', 'admin')
"""
cursor.execute(sql)

sql = """
    INSERT INTO admin (user_id)
    VALUES (2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Jim Haug', 'HS-KE', 3, 'admin')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (3, 'Standard', 'admin')
"""
cursor.execute(sql)

sql = """
    INSERT INTO admin (user_id)
    VALUES (3)
"""
cursor.execute(sql)


# Create course creator user
sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Julian Manz', 'HS-KE', 4, 'course creator')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (4, 'light', 'course creator')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_creator (user_id)
    VALUES (4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Marc Normann', 'TH-AB', 5, 'course creator')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (5, 'dark', 'course creator')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_creator (user_id)
    VALUES (5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Gesine Wagner', 'HS-KE', 6, 'course creator')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (6, 'Standard', 'course creator')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_creator (user_id)
    VALUES (6)
"""
cursor.execute(sql)


# Create student user
sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Emily Johnson', 'TH-AB', 7, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (7, 'light', 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (7)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Liam Anderson', 'HS-KE', 8, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (8, 'dark', 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (8)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Sophia Martinez', 'HS-RE', 9, 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (9, 'Standard', 'student')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student (user_id)
    VALUES (9)
"""
cursor.execute(sql)


# Create teacher user
sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Emma Johnson', 'TH-AB', 10, 'teacher')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (10, 'light', 'teacher')
"""
cursor.execute(sql)

sql = """
    INSERT INTO teacher (user_id)
    VALUES (10)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Liam Smith', 'HS-KE', 11, 'teacher')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (11, 'dark', 'teacher')
"""
cursor.execute(sql)

sql = """
    INSERT INTO teacher (user_id)
    VALUES (11)
"""
cursor.execute(sql)

sql = """
    INSERT INTO haski_user (name, university, lms_user_id, role)
    VALUES ('Sophia Martinez', 'HS-RE', 12, 'teacher')
"""
cursor.execute(sql)

sql = """
    INSERT INTO settings (user_id, theme, pswd)
    VALUES (12, 'Standard', 'teacher')
"""
cursor.execute(sql)

sql = """
    INSERT INTO teacher (user_id)
    VALUES (12)
"""
cursor.execute(sql)

# create courses
sql = """
    INSERT INTO course (lms_id, name, university)
    VALUES (2, 'Software Engineering', 'HS-RE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course (lms_id, name, university)
    VALUES (3, 'Software Architecture', 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_creator_course (course_creator_id, course_id,\
    created_at, last_updated)
    VALUES (1, 1, '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_creator_course (course_creator_id, course_id,\
    created_at, last_updated)
    VALUES (2, 2, '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

# create topics
sql = """
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
    created_by, created_at, last_updated)
    VALUES (1, true, true, 'General', 'HS-KE', '', '2023-07-13 16:00:00',\
    '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
    created_by, created_at, last_updated)
    VALUES (2, true, true, 'Metrics', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
    created_by, created_at, last_updated)
    VALUES (3, true, true, 'Something Else', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
    created_by, created_at, last_updated)
    VALUES (4, true, true, 'General', 'TH-AB', 'Marc Normann',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
    created_by, created_at, last_updated)
    VALUES (5, true, true, 'Design Pattern', 'TH-AB', 'Marc Normann',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
    created_by, created_at, last_updated)
    VALUES (6, true, false, 'Nothing else', 'TH-AB', 'Marc Normann',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
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
    VALUES (2, 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO course_topic (course_id, topic_id)
    VALUES (2, 6)
"""
cursor.execute(sql)

# create learning elements

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at,\
    last_updated)
    VALUES (1, 'h5pactivity', 'KÜ', 'Introduction', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (2, 'h5pactivity', 'EK', 'General Something', 'HS-KE',\
    'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (3, 'h5pactivity', 'ÜB', 'Metric-1', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (4, 'h5pactivity', 'ÜB', 'Metric-2', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (5, 'h5pactivity', 'ÜB', 'Something-Else-1', 'HS-KE',\
    'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (6, 'h5pactivity', 'ÜB', 'Something-Else-2', 'HS-KE',\
    'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (7, 'h5pactivity', 'KÜ', 'Einführung', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (8, 'h5pactivity', 'ÜB', 'Design Pattern Allgemein', 'HS-KE',\
    'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (9, 'h5pactivity', 'ÜB', 'Design Pattern Erweitert', 'HS-KE',\
    'Dimitri Bigler', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (10, 'h5pactivity', 'ÜB', 'Übung - 1', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element (lms_id, activity_type, classification, name,\
    university, created_by, created_at, last_updated)
    VALUES (11, 'h5pactivity', 'ÜB', 'Übung - 2', 'HS-KE', 'Dimitri Bigler',\
    '2023-07-13 16:00:00', '2023-07-20 20:00:00')
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
    VALUES (2, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (2, 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (3, 5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (3, 6)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (4, 7)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (5, 8)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (5, 9)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 10)
"""
cursor.execute(sql)

sql = """
    INSERT INTO topic_learning_element (topic_id, learning_element_id)
    VALUES (6, 11)
"""
cursor.execute(sql)

# create contactform
sql = """
    INSERT INTO contact_form (user_id, report_topic, report_type, date)
    VALUES (1, 'General Error', 'Elemente werden nicht angezeigt',\
    '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO contact_form (user_id, report_topic, report_type, date)
    VALUES (2, 'Bug', 'Wenn ich auf Button klicke, dann...',\
    '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO contact_form (user_id, report_topic, report_type, date)
    VALUES (3, 'Feedback', 'Übersicht verbessern', '2023-07-13 16:00:00')
"""
cursor.execute(sql)

# create logbuffer
sql = """
    INSERT INTO logbuffer (user_id, content, date)
    VALUES (1, 'Fehler beim Abrufen der Kursdaten',\
    '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO logbuffer (user_id, content, date)
    VALUES (5, 'Test buffer message. Error btw.',\
    '2023-07-13 16:00:00')
"""
cursor.execute(sql)

# create news
sql = """
    INSERT INTO news (language_id, news_content, expiration_date, created_at)
    VALUES ('de', 'Wir testen gerade die Seite', \
    '2025-04-20 16:00:00',\
    '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO news (language_id, news_content, expiration_date, created_at)
    VALUES ('en', 'Test for eng news', \
    '2025-04-15 16:00:00',\
    '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO news (language_id, news_content, university, expiration_date,\
    created_at)
    VALUES ('en', 'Test in en and with Kempten university', \
    'HS-KE', '2025-04-20 16:00:00',\
    '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO news (language_id, news_content, university, expiration_date,\
    created_at)
    VALUES ('en', 'Test in eng and with Aschaffenburg university', \
    'TH-AB', '2025-04-15 16:00:00',\
    '2023-07-13 16:00:00')
"""
cursor.execute(sql)

# Add student to course
sql = """
    INSERT INTO student_course (student_id, course_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (1, 1, 'act', 7, 'Sensory', 5, 'vis', 11, 'seq', 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course (student_id, course_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (2, 1, 'ref', 3, 'int', 7, 'vrb', 5, 'glo', 11)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course (student_id, course_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (2, 2, 'ref', 9, 'int', 3, 'vrb', 11, 'glo', 11)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_course (student_id, course_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (3, 2, 'act', 7, 'int', 3, 'vis', 7, 'glo', 11)
"""
cursor.execute(sql)


# Add teacher to course
sql = """
    INSERT INTO teacher_course (teacher_id, course_id)
    VALUES (1, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO teacher_course (teacher_id, course_id)
    VALUES (2, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO teacher_course (teacher_id, course_id)
    VALUES (3, 2)
"""
cursor.execute(sql)

# Add learning path to course / topic path
sql = """
    INSERT INTO learning_path (student_id, course_id, based_on)
    VALUES (1, 1, 'aco')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on)
    VALUES (1, 2, 'aco')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on)
    VALUES (2, 1, 'aco')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on)
    VALUES (2, 2, 'aco')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on)
    VALUES (3, 1, 'aco')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on)
    VALUES (3, 2, 'aco')
"""
cursor.execute(sql)

# Add learning path to course / element path
sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (1, 1, 'aco', 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (1, 1, 'aco', 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (1, 1, 'aco', 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (1, 2, 'aco', 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (1, 2, 'aco', 5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (1, 2, 'aco', 6)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (2, 1, 'aco', 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (2, 1, 'aco', 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (2, 1, 'aco', 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (2, 2, 'aco', 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (2, 2, 'aco', 5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (2, 2, 'aco', 6)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (3, 1, 'aco', 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (3, 1, 'aco', 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (3, 1, 'aco', 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (3, 2, 'aco', 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (3, 2, 'aco', 5)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path (student_id, course_id, based_on, topic_id)
    VALUES (3, 2, 'aco', 6)
"""
cursor.execute(sql)

# Topic path
sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (1, 1, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (2, 1, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (3, 1, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (4, 2, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (5, 2, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (6, 2, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (1, 3, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (2, 3, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (3, 3, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (4, 4, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (5, 4, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (6, 4, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (1, 5, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (2, 5, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (3, 5, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (4, 6, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (5, 6, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_topic (topic_id, learning_path_id, recommended,\
    position)
    VALUES (6, 6, false, 3)
"""
cursor.execute(sql)

# Element Path
sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (1, 7, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (2, 7, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (3, 8, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (4, 8, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (5, 9, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (6, 9, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (7, 10, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (8, 11, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (9, 11, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (10, 11, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (11, 12, false, 4)
"""
cursor.execute(sql)

###
sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (1, 13, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (2, 13, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (3, 14, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (4, 14, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (5, 15, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (6, 15, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (7, 16, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (8, 17, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (9, 17, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (10, 17, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (11, 17, false, 4)
"""
cursor.execute(sql)

###

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (1, 19, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (2, 19, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (3, 20, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (4, 20, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (5, 21, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (6, 21, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (7, 22, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (8, 23, true, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (9, 23, false, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (10, 23, false, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element (learning_element_id,\
    learning_path_id, recommended, position)
    VALUES (11, 23, false, 4)
"""
cursor.execute(sql)

# create Student visited learning element
sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 1, '2023-07-14 14:03:30', '2023-07-14 15:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 2, '2023-07-14 15:05:45', '2023-07-14 15:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 3, '2023-07-14 15:45:45', '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 4, '2023-07-14 16:05:45', '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 5, '2023-07-14 16:45:45', '2023-07-14 17:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 6, '2023-07-14 17:05:45', '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 7, '2023-07-14 17:45:45', '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 8, '2023-07-14 18:05:45', '2023-07-14 18:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 9, '2023-07-15 08:45:45', '2023-07-15 09:55:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 10, '2023-07-15 09:55:45', '2023-07-15 15:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (1, 11, '2023-07-16 14:03:30', '2023-07-16 14:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 1, '2023-07-14 16:03:30', '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 2, '2023-07-14 15:05:45', '2023-07-14 15:30:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 3, '2023-07-14 16:05:45', '2023-07-14 16:07:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 4, '2023-07-14 16:07:45', '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 5, '2023-07-14 16:45:45', '2023-07-14 17:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 6, '2023-07-14 17:05:45', '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 7, '2023-07-14 17:45:45', '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (2, 8, '2023-07-14 18:05:45', '2023-07-14 18:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (3, 1, '2023-07-14 16:03:30', '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (3, 2, '2023-07-14 15:05:45', '2023-07-14 15:30:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (3, 5, '2023-07-14 16:45:45', '2023-07-14 17:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (3, 6, '2023-07-14 17:05:45', '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element_visit (student_id,\
    learning_element_id, visit_start, visit_end)
    VALUES (3, 8, '2023-07-14 20:05:45', '2023-07-14 21:45:45')
"""
cursor.execute(sql)

# create Student completed learning element
sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 1, true, '2023-07-14 15:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 2, true, '2023-07-14 15:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 3, true, '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 4, true, '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 5, true, '2023-07-14 17:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 6, true, '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 7, true, '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 8, true, '2023-07-14 18:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 9, true, '2023-07-15 9:55:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 10, true, '2023-07-15 15:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (1, 11, true, '2023-07-16 14:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 1, true, '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 2, true, '2023-07-14 15:30:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 3, true, '2023-07-14 16:07:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 4, true, '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 5, true, '2023-07-14 17:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 6, true, '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 7, true, '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (2, 8, true, '2023-07-14 18:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (3, 1, true, '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (3, 2, true, '2023-07-14 15:30:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (3, 5, true, '2023-07-14 17:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (3, 6, true, '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_element (student_id, learning_element_id,\
    done, done_at)
    VALUES (3, 8, true, '2023-07-14 21:45:45')
"""
cursor.execute(sql)

# Student visited topic
sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (1, 1, '2023-07-14 14:03:30', '2023-07-14 15:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (1, 2, '2023-07-14 15:45:45', '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (1, 3, '2023-07-14 16:45:45', '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (1, 4, '2023-07-14 17:45:45', '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (1, 5, '2023-07-14 18:05:45', '2023-07-16 14:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (1, 6, '2023-07-16 14:05:45', '2023-07-16 14:05:47')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (2, 1, '2023-07-14 15:05:45', '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (2, 2, '2023-07-14 16:05:45', '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (2, 3, '2023-07-14 16:45:45', '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (2, 4, '2023-07-14 17:45:45', '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (2, 5, '2023-07-14 18:05:45', '2023-07-14 18:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (3, 1, '2023-07-14 15:05:45', '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (3, 3, '2023-07-14 16:45:45', '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic_visit (student_id, topic_id, visit_start,\
    visit_end)
    VALUES (3, 5, '2023-07-14 20:05:45', '2023-07-14 21:45:45')
"""
cursor.execute(sql)

# Student completed topic
sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (1, 1, true, '2023-07-14 15:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (1, 2, true, '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (1, 3, true, '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (1, 4, true, '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (1, 5, true, '2023-07-16 14:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (1, 6, true, '2023-07-16 14:05:47')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (2, 1, true, '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (2, 2, true, '2023-07-14 16:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (2, 3, true, '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (2, 4, true, '2023-07-14 18:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (2, 5, true, '2023-07-14 18:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (3, 1, true, '2023-07-14 16:05:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (3, 3, true, '2023-07-14 17:45:45')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_topic (student_id, topic_id, done, done_at)
    VALUES (3, 5, true, '2023-07-14 21:45:45')
"""
cursor.execute(sql)

# create learning_characteristics
sql = """
    INSERT INTO learning_characteristics (student_id)
    VALUES (1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_characteristics (student_id)
    VALUES (2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_characteristics (student_id)
    VALUES (3)
"""
cursor.execute(sql)

# create learning_strategy
sql = """
    INSERT INTO learning_strategy (characteristic_id, cogn_str, org, elab,\
    crit_rev, rep, metacogn_str, goal_plan, con, reg, int_res_mng_str,\
    att, eff, time, ext_res_mng_str, lrn_w_cls, lit_res, lrn_env)
    VALUES (1, 1.33, 2.33, 3.33, 4.33, 1.33, 2.33, 3.33, 4.33, 1.33, 2.33,\
    3.33, 4.33, 1.33, 2.33, 3.33, 4.33, 1.33)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_strategy (characteristic_id, cogn_str, org, elab,\
    crit_rev, rep, metacogn_str, goal_plan, con, reg, int_res_mng_str,\
    att, eff, time, ext_res_mng_str, lrn_w_cls, lit_res, lrn_env)
    VALUES (2, 1.67, 2.67, 3.74, 4.84, 2.45, 2.88, 3.78, 4.77, 1.48, 2.88,\
    3.03, 4.79, 1.50, 2.78, 3.99, 4.04, 1.79)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_strategy (characteristic_id, cogn_str, org, elab,\
    crit_rev, rep, metacogn_str, goal_plan, con, reg, int_res_mng_str,\
    att, eff, time, ext_res_mng_str, lrn_w_cls, lit_res, lrn_env)
    VALUES (3, 4.67, 3.67, 2.74, 1.84, 2.45, 4.88, 1.78, 1.77, 5.00, 3.88,\
    3.03, 4.79, 1.50, 1.78, 2.99, 2.04, 1.79)
"""
cursor.execute(sql)

# create learning_style
sql = """
    INSERT INTO learning_style (characteristic_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (1, 'sns', 7, 'vis', 3, 'act', 9, 'seq', 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_style (characteristic_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (2, 'sns', 7, 'vis', 5, 'act', 11, 'glo', 11)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_style (characteristic_id, perception_dimension,\
    perception_value, input_dimension, input_value, processing_dimension,\
    processing_value, understanding_dimension, understanding_value)
    VALUES (3, 'sns', 1, 'vrb', 11, 'ref', 3, 'glo', 1)
"""
cursor.execute(sql)

# create ils questionnaire answers
sql = """
    INSERT INTO questionnaire_ils (student_id)
    VALUES (1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_input_answers (questionnaire_ils_id, vv_1_f3, vv_2_f7,\
    vv_3_f11, vv_4_f15, vv_5_f19, vv_6_f23, vv_7_f27, vv_8_f31, vv_9_f35,\
    vv_10_f39, vv_11_f43)
    VALUES (1, 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_perception_answers (questionnaire_ils_id, si_1_f2,
    si_2_f6, si_3_f10, si_4_f14, si_5_f18, si_6_f22, si_7_f26, si_8_f30,\
    si_9_f34, si_10_f38, si_11_f42)
    VALUES (1, 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_processing_answers (questionnaire_ils_id, ar_1_f1,\
    ar_2_f5, ar_3_f9, ar_4_f13, ar_5_f17, ar_6_f21, ar_7_f25, ar_8_f29,\
    ar_9_f33, ar_10_f37, ar_11_f41)
    VALUES (1, 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_understanding_answers (questionnaire_ils_id, sg_1_f4,\
    sg_2_f8, sg_3_f12, sg_4_f16, sg_5_f20, sg_6_f24, sg_7_f28, sg_8_f32,\
    sg_9_f36, sg_10_f40, sg_11_f44)
    VALUES (1, 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')
"""
cursor.execute(sql)

sql = """
    INSERT INTO questionnaire_ils (student_id)
    VALUES (2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_input_answers (questionnaire_ils_id, vv_1_f3, vv_2_f7,\
    vv_3_f11, vv_4_f15, vv_5_f19, vv_6_f23, vv_7_f27, vv_8_f31, vv_9_f35,\
    vv_10_f39, vv_11_f43)
    VALUES (2, 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_perception_answers (questionnaire_ils_id, si_1_f2, si_2_f6,\
    si_3_f10, si_4_f14, si_5_f18, si_6_f22, si_7_f26, si_8_f30, si_9_f34,\
    si_10_f38, si_11_f42)
    VALUES (2, 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_processing_answers (questionnaire_ils_id, ar_1_f1,\
    ar_2_f5, ar_3_f9, ar_4_f13, ar_5_f17, ar_6_f21, ar_7_f25, ar_8_f29,\
    ar_9_f33, ar_10_f37, ar_11_f41)
    VALUES (2, 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_understanding_answers (questionnaire_ils_id, sg_1_f4,\
    sg_2_f8, sg_3_f12, sg_4_f16, sg_5_f20, sg_6_f24, sg_7_f28, sg_8_f32,\
    sg_9_f36, sg_10_f40, sg_11_f44)
    VALUES (2, 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')
"""
cursor.execute(sql)

sql = """
    INSERT INTO questionnaire_ils (student_id)
    VALUES (3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_input_answers (questionnaire_ils_id, vv_1_f3, vv_2_f7,\
    vv_3_f11, vv_4_f15, vv_5_f19, vv_6_f23, vv_7_f27, vv_8_f31, vv_9_f35,\
    vv_10_f39, vv_11_f43)
    VALUES (3, 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_perception_answers (questionnaire_ils_id, si_1_f2,\
    si_2_f6, si_3_f10, si_4_f14, si_5_f18, si_6_f22, si_7_f26, si_8_f30,\
    si_9_f34, si_10_f38, si_11_f42)
    VALUES (3, 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_processing_answers (questionnaire_ils_id, ar_1_f1,\
    ar_2_f5, ar_3_f9, ar_4_f13, ar_5_f17, ar_6_f21, ar_7_f25, ar_8_f29,\
    ar_9_f33, ar_10_f37, ar_11_f41)
    VALUES (3, 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a')
"""
cursor.execute(sql)

sql = """
    INSERT INTO ils_understanding_answers (questionnaire_ils_id, sg_1_f4,\
    sg_2_f8, sg_3_f12, sg_4_f16, sg_5_f20, sg_6_f24, sg_7_f28, sg_8_f32,\
    sg_9_f36, sg_10_f40, sg_11_f44)
    VALUES (3, 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')
"""
cursor.execute(sql)

# Create questionnaire list k
sql = """
    INSERT INTO questionnaire_list_k (student_id, org1_f1, org2_f2, org3_f3,\
    elab1_f4, elab2_f5, elab3_f6, crit_rev1_f7, crit_rev2_f8, crit_rev3_f9,\
    rep1_f10, rep2_f11, rep3_f12, goal_plan1_f13, goal_plan2_f14,\
    goal_plan3_f15, con1_f16, con2_f17, con3_f18, reg1_f19, reg2_f20,\
    reg3_f21, att1_f22, att2_f23, att3_f24, eff1_f25, eff2_f26, eff3_f27,\
    time1_f28, time2_f29, time3_f30, lrn_w_cls1_f31, lrn_w_cls2_f32,\
    lrn_w_cls3_f33, lit_res1_f34, lit_res2_f35, lit_res3_f36, lrn_env1_f37,\
    lrn_env2_f38, lrn_env3_f39)
    VALUES (1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,\
    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO questionnaire_list_k (student_id, org1_f1, org2_f2, org3_f3,\
    elab1_f4, elab2_f5, elab3_f6, crit_rev1_f7, crit_rev2_f8, crit_rev3_f9,\
    rep1_f10, rep2_f11, rep3_f12, goal_plan1_f13, goal_plan2_f14,\
    goal_plan3_f15, con1_f16, con2_f17, con3_f18, reg1_f19, reg2_f20,\
    reg3_f21, att1_f22, att2_f23, att3_f24, eff1_f25, eff2_f26, eff3_f27,\
    time1_f28, time2_f29, time3_f30, lrn_w_cls1_f31, lrn_w_cls2_f32,\
    lrn_w_cls3_f33, lit_res1_f34, lit_res2_f35, lit_res3_f36, lrn_env1_f37,\
    lrn_env2_f38, lrn_env3_f39)
    VALUES (2, 3, 5, 3, 1, 1, 2, 3, 3, 5, 3, 4, 3, 3, 1, 2, 3, 5, 3, 4, 3, 2,\
    3, 1, 3, 5, 3, 1, 3, 3, 3, 2, 3, 5, 3, 5, 3, 1, 3, 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO questionnaire_list_k (student_id, org1_f1, org2_f2, org3_f3,\
    elab1_f4, elab2_f5, elab3_f6, crit_rev1_f7, crit_rev2_f8, crit_rev3_f9,\
    rep1_f10, rep2_f11, rep3_f12, goal_plan1_f13, goal_plan2_f14,\
    goal_plan3_f15, con1_f16, con2_f17, con3_f18, reg1_f19, reg2_f20,\
    reg3_f21, att1_f22, att2_f23, att3_f24, eff1_f25, eff2_f26, eff3_f27,\
    time1_f28, time2_f29, time3_f30, lrn_w_cls1_f31, lrn_w_cls2_f32,\
    lrn_w_cls3_f33, lit_res1_f34, lit_res2_f35, lit_res3_f36, lrn_env1_f37,\
    lrn_env2_f38, lrn_env3_f39)
    VALUES (3, 1, 1, 3, 1, 1, 2, 3, 3, 5, 3, 4, 3, 3, 1, 2, 3, 5, 3, 4, 3, 2,\
    3, 1, 3, 5, 3, 1, 3, 3, 3, 2, 3, 5, 3, 5, 4, 5, 5, 1)
"""
cursor.execute(sql)

# Create Knowledge
sql = """
    INSERT INTO knowledge (characteristic_id)
    VALUES (1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO knowledge (characteristic_id)
    VALUES (2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO knowledge (characteristic_id)
    VALUES (3)
"""
cursor.execute(sql)

# Create Learning analytics
sql = """
    INSERT INTO learning_analytics (characteristic_id)
    VALUES (1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_analytics (characteristic_id)
    VALUES (2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_analytics (characteristic_id)
    VALUES (3)
"""
cursor.execute(sql)

# Create default learning path for HS-KE
sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('KÜ', 1, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('EK', 2, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('AN', 3, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('SE', 4, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('BE', 5, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('ÜB', 6, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('ZF', 7, 'HS-KE')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('ZL', 8, 'HS-KE')
"""
cursor.execute(sql)

# Create default learning path for TH-AB
sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('KÜ', 1, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('ZL', 2, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('EK', 3, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('AN', 4, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('BE', 5, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('SE', 6, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('AB', 7, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('ÜB', 8, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('LZ', 9, 'TH-AB')
"""
cursor.execute(sql)

sql = """
    INSERT INTO default_learning_path (classification, position, university)
    VALUES ('ZF', 10, 'TH-AB')
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

# create default learning path algorithm for the topics
sql = """
    INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)
    VALUES (1, 1)
    """
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)
    VALUES (2, 1)
    """
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)
    VALUES (3, 1)
    """
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)
    VALUES (4, 2)
    """
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)
    VALUES (5, 3)
    """
cursor.execute(sql)

sql = """
    INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)
    VALUES (6, 4)
    """
cursor.execute(sql)

# Create learning path algorithms per student per topic
sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (1, 1, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (1, 2, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (1, 3, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (1, 4, 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (1, 5, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (1, 6, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (2, 1, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (2, 2, 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (2, 3, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (2, 4, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (2, 5, 3)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (3, 1, 4)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (3, 3, 1)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_learning_path_learning_element_algorithm (\
    student_id, topic_id, algorithm_id)
    VALUES (3, 5, 2)
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_rating (\
    student_id, topic_id, rating_value, rating_deviation, timestamp)
    VALUES (7, 1, 1500, 350, '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO student_rating (\
    student_id, topic_id, rating_value, rating_deviation, timestamp)
    VALUES (7, 2, 1500, 350, '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element_rating (\
    learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
    VALUES (1, 1, 1500, 350, '2023-07-13 16:00:00')
"""
cursor.execute(sql)

sql = """
    INSERT INTO learning_element_rating (\
    learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
    VALUES (1, 2, 1500, 350, '2023-07-13 16:00:00')
"""
cursor.execute(sql)

conn.commit()
# Closing the connection
conn.close()
