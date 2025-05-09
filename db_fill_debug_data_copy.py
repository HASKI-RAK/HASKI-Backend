import argparse
import os

import psycopg2
from dotenv import load_dotenv

load_dotenv(".flaskenv")
load_dotenv()

DEFAULT_DB_HOST = "localhost"
DEFAULT_DB_PORT = 5432
DEFAULT_DB_PASSWORD = "postgres"  # Does not matter for local development
DEFAULT_DB_USER = "postgres"
DEFAULT_DB_NAME = "haski_3"


def setup_db(
        db_database=DEFAULT_DB_NAME,
        db_user=DEFAULT_DB_USER,
        db_password=DEFAULT_DB_PASSWORD,
        db_host=DEFAULT_DB_HOST,
        db_port=DEFAULT_DB_PORT,
):

    # Establishing the connection
    conn = psycopg2.connect(
        database=db_database,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
    )
    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Fill Database with example data. Insert the following data into DB:

    # Create user
    sql = """
        INSERT INTO haski_user (name, university, lms_user_id, role)
        VALUES ('Example Course Creator', 'HS-KE', 1, 'course creator')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO settings (user_id, theme, pswd)
        VALUES (1, 'HaskiTheme', '')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO haski_user (name, university, lms_user_id, role)
        VALUES ('Example Student One', 'HS-KE', 2, 'student')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO settings (user_id, theme, pswd)
        VALUES (2, 'DarkTheme', '')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO haski_user (name, university, lms_user_id, role)
        VALUES ('Example Student Two', 'HS-KE', 3, 'student')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO settings (user_id, theme, pswd)
        VALUES (3, 'AltTheme', '')
    """
    cursor.execute(sql)


    # Create course creator user
    sql = """
        INSERT INTO course_creator (user_id)
        VALUES (1)
    """
    cursor.execute(sql)

    # Create student user
    sql = """
        INSERT INTO student (user_id)
        VALUES (1)
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


    # create courses
    sql = """
        INSERT INTO course (lms_id, name, university, start_date)
        VALUES (2, 'Software Engineering', 'HS-KE', '2025-03-24 14:52:51')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO course (lms_id, name, university, start_date)
        VALUES (3, 'Software Architecture', 'HS-KE', '2025-03-24 14:52:51')
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO course (lms_id, name, university, start_date)
          VALUES (4, 'Example Disabled Course', 'HS-KE', '3025-12-24 20:00:00') \
          """
    cursor.execute(sql)

    sql = """
        INSERT INTO course_creator_course (course_creator_id, course_id,\
        created_at)
        VALUES (1, 1, '2025-03-24 15:52:56')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO course_creator_course (course_creator_id, course_id,\
        created_at)
        VALUES (1, 1, '2025-03-24 15:53:56')
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO course_creator_course (course_creator_id, course_id, \
                                             created_at)
          VALUES (1, 1, '2025-03-24 15:54:56') \
          """
    cursor.execute(sql)

    # create topics
    sql = """
        INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
        created_by, created_at, last_updated)
        VALUES (1, true, true, 'General', 'HS-KE', 'Example Course Creator', 
                '2025-03-13 16:00:00', '2025-03-20 20:00:00')
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO topic (lms_id, is_topic, contains_le, name, university, \
                             created_by, created_at, last_updated)
          VALUES (2, true, true, 'Entwurfsmuster', 'HS-KE', 'Example Course Creator',
                  '2025-03-13 16:10:00', '2025-03-20 20:10:00') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO topic (lms_id, is_topic, contains_le, name, university, \
                             created_by, created_at, last_updated)
          VALUES (3, true, true, 'Metriken', 'HS-KE', 'Example Course Creator',
                  '2025-03-13 16:20:00', '2025-03-20 20:20:00') \
          """
    cursor.execute(sql)

    sql = """
        INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
        created_by, created_at, last_updated)
        VALUES (4, true, true, 'General', 'HS-KE', 'Example Course Creator',\
        '2025-03-13 16:30:00', '2025-03-20 20:30:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
        created_by, created_at, last_updated)
        VALUES (5, true, true, 'Schichtenarchitektur', 'HS-KE', 'Example Course Crator',\
        '2025-03-13 16:40:00', '2025-03-20 20:40:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO topic (lms_id, is_topic, contains_le, name, university,\
        created_by, created_at, last_updated)
        VALUES (6, true, false, 'Architektur Prinzipien', 'HS-KE', 'Example Course Creator',\
        '2025-03-13 16:50:00', '2025-03-20 20:50:00')
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
        VALUES (1, 'h5pactivity', 'KÜ', 'Kurzübersicht', 'HS-KE', 'Example Course Creator',\
        '2023-07-13 16:00:00', '2023-07-20 20:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element (lms_id, activity_type, classification, name,\
        university, created_by, created_at, last_updated)
        VALUES (2, 'h5pactivity', 'EK', 'Einführungsvideo', 'HS-KE',\
        'Example Course Creator', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, last_updated)
          VALUES (3, 'h5pactivity', 'AB', 'Zustandsmuster', 'HS-KE', \
                  'Example Course Creator', '2023-07-13 16:00:00', '2023-07-20 20:00:00') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, last_updated)
          VALUES (4, 'h5pactivity', 'AB', 'Adaptermuster', 'HS-KE', \
                  'Example Course Creator', '2023-07-13 16:00:00', '2023-07-20 20:00:00') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, \
                                        last_updated)
          VALUES (5, 'h5pactivity', 'KÜ', 'Kurzübersicht', 'HS-KE', 'Example Course Creator', \
                  '2023-07-13 16:00:00', '2023-07-20 20:00:00') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, last_updated)
          VALUES (6, 'h5pactivity', 'EK', 'Einführungsvideo', 'HS-KE', \
                  'Example Course Creator', '2023-07-13 16:00:00', '2023-07-20 20:00:00') \
          """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element (lms_id, activity_type, classification, name,\
        university, created_by, created_at, last_updated)
        VALUES (7, 'h5pactivity', 'ÜB', 'Lines of Code 1', 'HS-KE', 'Example Course Creator',\
        '2023-07-13 16:00:00', '2023-07-20 20:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element (lms_id, activity_type, classification, name,\
        university, created_by, created_at, last_updated)
        VALUES (8, 'h5pactivity', 'ÜB', 'Halstead-Metrik', 'HS-KE', 'Example Course Creator',\
        '2023-07-13 16:00:00', '2023-07-20 20:00:00')
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, \
                                        last_updated)
          VALUES (9, 'h5pactivity', 'KÜ', 'Kurzübersicht', 'HS-KE', 'Example Course Creator', \
                  '2023-07-13 16:00:00', '2023-07-20 20:00:00') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, last_updated)
          VALUES (10, 'h5pactivity', 'EK', 'Einführungsvideo', 'HS-KE', \
                  'Example Course Creator', '2023-07-13 16:00:00', '2023-07-20 20:00:00') \
          """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element (lms_id, activity_type, classification, name,\
        university, created_by, created_at, last_updated)
        VALUES (11, 'h5pactivity', 'ÜB', 'Layerbridging', 'HS-KE',\
        'Example Course Creator', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element (lms_id, activity_type, classification, name,\
        university, created_by, created_at, last_updated)
        VALUES (12, 'h5pactivity', 'KÜ', 'Einführung', 'HS-KE', 'Example Course Creator',\
        '2023-07-13 16:00:00', '2023-07-20 20:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element (lms_id, activity_type, classification, name,\
        university, created_by, created_at, last_updated)
        VALUES (13, 'h5pactivity', 'BE', 'Lose Kopplung', 'HS-KE',\
        'Example Course Creator', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element (lms_id, activity_type, classification, name,\
        university, created_by, created_at, last_updated)
        VALUES (14, 'h5pactivity', 'BE', 'Hohe Kohäsion', 'HS-KE',\
        'Example Course Creator', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element (lms_id, activity_type, classification, name,\
        university, created_by, created_at, last_updated)
        VALUES (15, 'h5pactivity', 'BE', 'Seperation of Concerns', 'HS-KE', 'Example Course Creator',\
        '2023-07-13 16:00:00', '2023-07-20 20:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element (lms_id, activity_type, classification, name,\
        university, created_by, created_at, last_updated)
        VALUES (16, 'h5pactivity', 'ÜB', 'Open Closed Principles', 'HS-KE', 
                'Example Course Creator', '2023-07-13 16:00:00', '2023-07-20 20:00:00')
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, last_updated)
          VALUES (17, 'h5pactivity', 'FO', 'Forum', 'HS-KE',
                  'Example Course Creator', '2023-07-13 16:00:00', '2023-07-20 20:00:00') \
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
        VALUES (3, 7)
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO topic_learning_element (topic_id, learning_element_id)
        VALUES (3, 8)
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO topic_learning_element (topic_id, learning_element_id)
        VALUES (4, 9)
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO topic_learning_element (topic_id, learning_element_id)
        VALUES (4, 10)
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO topic_learning_element (topic_id, learning_element_id)
        VALUES (5, 11)
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO topic_learning_element (topic_id, learning_element_id)
          VALUES (6, 12) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO topic_learning_element (topic_id, learning_element_id)
          VALUES (6, 13) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO topic_learning_element (topic_id, learning_element_id)
          VALUES (6, 14) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO topic_learning_element (topic_id, learning_element_id)
          VALUES (6, 15) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO topic_learning_element (topic_id, learning_element_id)
          VALUES (6, 16) \
          """
    cursor.execute(sql)

    # Learning Element will not be in the default learning path
    sql = """
          INSERT INTO topic_learning_element (topic_id, learning_element_id)
          VALUES (6, 17) \
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
        VALUES (1, 'Wed, 26 Mar 2025 14:53:35 GMT', \
                '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO logbuffer (user_id, content, date)
        VALUES (2, 'Test buffer message. Error btw.',\
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

    # Add student to course
    sql = """
        INSERT INTO student_course (student_id, course_id, perception_dimension,\
        perception_value, input_dimension, input_value, processing_dimension,\
        processing_value, understanding_dimension, understanding_value)
        VALUES (1, 1, 'act', 7, 'Sensory', 5, 'vis', 11, 'seq', 3)
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_course (student_id, course_id, perception_dimension, \
          perception_value, input_dimension, input_value, processing_dimension, \
          processing_value, understanding_dimension, understanding_value)
          VALUES (1, 2, 'act', 7, 'Sensory', 5, 'vis', 11, 'seq', 3) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_course (student_id, course_id, perception_dimension, \
          perception_value, input_dimension, input_value, processing_dimension, \
          processing_value, understanding_dimension, understanding_value)
          VALUES (1, 3, 'act', 7, 'Sensory', 5, 'vis', 11, 'seq', 3) \
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
        VALUES (2, 2, 'ref', 3, 'int', 7, 'vrb', 5, 'glo', 11)
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_course (student_id, course_id, perception_dimension, \
          perception_value, input_dimension, input_value, processing_dimension, \
          processing_value, understanding_dimension, understanding_value)
          VALUES (2, 3, 'ref', 3, 'int', 7, 'vrb', 5, 'glo', 11) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_course (student_id, course_id, perception_dimension, \
          perception_value, input_dimension, input_value, processing_dimension, \
          processing_value, understanding_dimension, understanding_value)
          VALUES (3, 1, 'act', 7, 'int', 3, 'vis', 7, 'glo', 11) \
          """
    cursor.execute(sql)

    sql = """
        INSERT INTO student_course (student_id, course_id, perception_dimension,\
        perception_value, input_dimension, input_value, processing_dimension,\
        processing_value, understanding_dimension, understanding_value)
        VALUES (3, 2, 'act', 7, 'int', 3, 'vis', 7, 'glo', 11)
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_course (student_id, course_id, perception_dimension, \
          perception_value, input_dimension, input_value, processing_dimension, \
          processing_value, understanding_dimension, understanding_value)
          VALUES (3, 3, 'act', 7, 'int', 3, 'vis', 7, 'glo', 11) \
          """
    cursor.execute(sql)


    # Add learning path to course / topic path
    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (1, 1, 'aco', 1, '2025-04-16 09:45:26+02')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (1, 1, 'default', 2, '2025-04-16 09:45:26+02')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (1, 1, 'graf', 3, '2025-04-16 09:45:26+02')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (1, 2, 'aco', 4, '2025-04-16 09:45:26+02')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (1, 2, 'graf', 5, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (1, 2, 'default', 6, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (2, 1, 'aco', 1, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (2, 1, 'default', 2, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (2, 1, 'graf', 3, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (2, 2, 'aco', 4, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (2, 2, 'graf', 5, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (2, 2, 'default', 6, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (3, 1, 'aco', 1, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (3, 1, 'default', 2, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (3, 1, 'graf', 3, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (3, 2, 'aco', 4, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (3, 2, 'graf', 5, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path (student_id, course_id, based_on, topic_id, calculated_on)
        VALUES (3, 2, 'default', 6, '2025-04-16 09:45:26+02') \
    """
    cursor.execute(sql)


    # Element Path
    sql = """
        INSERT INTO learning_path_learning_element (learning_element_id,\
        learning_path_id, recommended, position)
        VALUES (1, 1, true, 1)
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
          learning_path_id, recommended, position)
          VALUES (2, 1, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
          learning_path_id, recommended, position)
          VALUES (1, 7, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
          learning_path_id, recommended, position)
          VALUES (2, 7, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
          learning_path_id, recommended, position)
          VALUES (1, 13, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
          learning_path_id, recommended, position)
          VALUES (2, 13, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
          learning_path_id, recommended, position)
          VALUES (3, 2, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
          learning_path_id, recommended, position)
          VALUES (4, 2, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
          learning_path_id, recommended, position)
          VALUES (3, 8, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
          learning_path_id, recommended, position)
          VALUES (4, 8, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
          learning_path_id, recommended, position)
          VALUES (3, 14, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
          learning_path_id, recommended, position)
          VALUES (4, 14, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (5, 3, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (6, 3, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (7, 3, true, 3) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (8, 3, true, 4) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (5, 9, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (6, 9, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (7, 9, true, 3) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (8, 9, true, 4) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (5, 15, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (6, 15, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (7, 15, true, 3) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (8, 15, true, 4) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (9, 4, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (10, 4, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (9, 10, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (10, 10, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (9, 16, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (10, 16, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (11, 5, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (11, 11, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (11, 17, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (12, 6, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (13, 6, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (14, 6, true, 3) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (15, 6, true, 4) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (16, 6, true, 5) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (17, 6, true, 6) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (12, 12, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (13, 12, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (14, 12, true, 3) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (15, 12, true, 4) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (16, 12, true, 5) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (17, 12, true, 6) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (12, 18, true, 1) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (13, 18, true, 2) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (14, 18, true, 3) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (15, 18, true, 4) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (16, 18, true, 5) \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, recommended, position)
          VALUES (17, 18, true, 6) \
          """
    cursor.execute(sql)


    # create Student completed learning element
    sql = """
        INSERT INTO student_learning_element (student_id, learning_element_id,\
        done, done_at)
        VALUES (1, 1, false, '2025-07-14 15:05:45')
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 2, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 3, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 4, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 5, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 6, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 7, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 8, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 9, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 10, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 11, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 12, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 13, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 14, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 15, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 16, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (1, 17, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 1, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 2, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 3, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 4, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 5, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 6, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 7, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 8, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 9, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 10, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 11, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 12, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 13, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 14, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 15, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 16, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (2, 17, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 1, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 2, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 3, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 4, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 5, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 6, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 7, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 8, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 9, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 10, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 11, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 12, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 13, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 14, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 15, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 16, false, '2025-07-14 15:05:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
                                                done, done_at)
          VALUES (3, 17, false, '2025-07-14 15:05:45') \
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
          VALUES (1, 2, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (1, 3, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (1, 4, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (1, 5, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (1, 6, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (2, 1, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (2, 2, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (2, 3, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (2, 4, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (2, 5, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (2, 6, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (3, 1, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (3, 2, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (3, 3, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (3, 4, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (3, 5, true, '2023-07-14 15:45:45') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, done_at)
          VALUES (3, 6, true, '2023-07-14 15:45:45') \
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

    sql = """
          INSERT INTO default_learning_path (classification, position, university)
          VALUES ('AB', 9, 'HS-KE') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO default_learning_path (classification, position, university)
          VALUES ('LZ', 10, 'HS-KE') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO default_learning_path (classification, position, university)
          VALUES ('RQ', 11, 'HS-KE') \
          """
    cursor.execute(sql)

    sql = """
          INSERT INTO default_learning_path (classification, position, university)
          VALUES ('FO', 9000, 'HS-KE') \
          """
    cursor.execute(sql)

    # create default learning path algorithm for the topics
    sql = """
        INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)
        VALUES (1, 2)
        """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)
        VALUES (2, 1)
        """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)
        VALUES (3, 4)
        """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)
        VALUES (4, 2)
        """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)
        VALUES (5, 4)
        """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)
        VALUES (6, 1)
        """
    cursor.execute(sql)

    # Create learning path algorithms per student per topic
    sql = """
        INSERT INTO student_learning_path_learning_element_algorithm (\
        student_id, topic_id, algorithm_id)
        VALUES (1, 1, 2)
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO student_learning_path_learning_element_algorithm (\
        student_id, topic_id, algorithm_id)
        VALUES (1, 2, 1)
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO student_learning_path_learning_element_algorithm (\
        student_id, topic_id, algorithm_id)
        VALUES (1, 3, 4)
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO student_learning_path_learning_element_algorithm (\
        student_id, topic_id, algorithm_id)
        VALUES (1, 4, 2)
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO student_learning_path_learning_element_algorithm (\
        student_id, topic_id, algorithm_id)
        VALUES (1, 5, 4)
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO student_learning_path_learning_element_algorithm (\
        student_id, topic_id, algorithm_id)
        VALUES (1, 6, 1)
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
          VALUES (2, 6, 3)
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
        VALUES (3, 2, 1)
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO student_learning_path_learning_element_algorithm (\
        student_id, topic_id, algorithm_id)
        VALUES (3, 3, 2)
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_path_learning_element_algorithm (\
          student_id, topic_id, algorithm_id)
          VALUES (3, 4, 4)
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_path_learning_element_algorithm (\
          student_id, topic_id, algorithm_id)
          VALUES (3, 5, 1)
    """
    cursor.execute(sql)

    sql = """
          INSERT INTO student_learning_path_learning_element_algorithm (\
          student_id, topic_id, algorithm_id)
          VALUES (3, 6, 2)
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO student_rating (\
        student_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (1, 1, 1500, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO student_rating (\
        student_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (2, 2, 1700, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)


    sql = """
          INSERT INTO student_rating (\
          student_id, topic_id, rating_value, rating_deviation, timestamp)
          VALUES (3, 2, 1150, 350, '2023-07-13 16:00:00')
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
        VALUES (2, 1, 1450, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating (\
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (3, 2, 1520, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating ( \
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (4, 2, 1400, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating ( \
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (5, 3, 1500, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating ( \
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (6, 3, 1500, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating ( \
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (7, 3, 1500, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating ( \
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (8, 3, 1500, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating ( \
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (9, 4, 1500, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating ( \
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (10, 4, 1500, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating ( \
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (11, 5, 1500, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating ( \
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (12, 6, 1500, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating ( \
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (13, 6, 1500, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating ( \
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (14, 6, 1500, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating ( \
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (15, 6, 1500, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    sql = """
        INSERT INTO learning_element_rating ( \
        learning_element_id, topic_id, rating_value, rating_deviation, timestamp)
        VALUES (16, 6, 1500, 350, '2023-07-13 16:00:00')
    """
    cursor.execute(sql)

    conn.commit()
    # Closing the connection
    conn.close()

def parse_args(parser=argparse.ArgumentParser()):
    parser.add_argument(
        "--host",
        type=str,
        default=os.environ.get("DB_HOST", DEFAULT_DB_HOST),
        help="Database host address",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=os.environ.get("DB_PORT", DEFAULT_DB_PORT),
        help="Database port",
    )
    parser.add_argument(
        "--user",
        type=str,
        default=os.environ.get("DB_USER", DEFAULT_DB_USER),
        help="Database user. Not pgadmin user",
    )
    parser.add_argument(
        "--password",
        type=str,
        default=os.environ.get("DB_PASSWORD", DEFAULT_DB_PASSWORD),
        help="Database password. Not pgadmin password",
    )
    parser.add_argument(
        "--dbname",
        type=str,
        default=os.environ.get("DB_NAME", DEFAULT_DB_NAME),
        help="Database name. Will be used across the project",
    )
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    setup_db(args.dbname, args.user, args.password, args.host, args.port)