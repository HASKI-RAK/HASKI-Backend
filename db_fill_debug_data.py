import argparse
import os

import psycopg2
from dotenv import load_dotenv

load_dotenv(".flaskenv")
load_dotenv()

DEFAULT_DB_HOST = "localhost"
DEFAULT_DB_PORT = 5432
# NOSONAR
DEFAULT_DB_PASSWORD = "postgres"  # Does not matter for local development
DEFAULT_DB_USER = "postgres"
DEFAULT_DB_NAME = "haski"


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

    # Create admin user
    sql = """
          INSERT INTO haski_user (name, university, lms_user_id, role)
          VALUES ('Admin User', 'HS-KE', 2, 'course creator');

          INSERT INTO haski_user (name, university, lms_user_id, role)
          VALUES ('Admin User-2', 'HS-KE', 3, 'course creator');

          INSERT INTO haski_user (name, university, lms_user_id, role)
          VALUES ('Student', 'HS-KE', 4, 'student');

          INSERT INTO haski_user (name, university, lms_user_id, role)
          VALUES ('Student-2', 'HS-KE', 5, 'student');
    """
    cursor.execute(sql)

    # Create course
    sql = """
          INSERT INTO course (lms_id, name, university, start_date)
          VALUES (2, 'Software Engineering', 'HS-KE', '2025-05-09 10:42:51');

          INSERT INTO course (lms_id, name, university, start_date)
          VALUES (3, 'Software Architektur', 'HS-KE', '2025-05-12 08:36:03');

          INSERT INTO course (lms_id, name, university, start_date)
          VALUES (4, 'Software Testing', 'HS-KE', '2125-05-12 08:36:03');
    """
    cursor.execute(sql)

    # Create course creator
    sql = """
          INSERT INTO course_creator (user_id) VALUES (1);

          INSERT INTO course_creator (user_id) VALUES (2);
    """
    cursor.execute(sql)

    # Create course creator course (who created which course)
    sql = """
          INSERT INTO course_creator_course (course_creator_id, course_id,\
                                             created_at, last_updated)
          VALUES (1, 1, '2025-05-09 12:43:15', NULL);

          INSERT INTO course_creator_course (course_creator_id, course_id,\
                                             created_at, last_updated)
          VALUES (2, 2, '2025-05-12 10:36:07', NULL);

          INSERT INTO course_creator_course (course_creator_id, course_id,\
                                             created_at, last_updated)
          VALUES (1, 3, '2025-05-12 10:38:07', NULL);
    """
    cursor.execute(sql)

    # Create topics
    sql = """
          INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, \
                             university, created_by, created_at, last_updated)
          VALUES (1, true, NULL, true, 'Entwurfsmuster', 'HS-KE', 'Admin User', \
                  '2025-05-09 00:00:00', NULL);

          INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name,\
                             university, created_by, created_at, last_updated)
          VALUES (3, true, NULL, true, 'Metriken', 'HS-KE', 'Admin User', \
                  '2025-05-12 00:00:00', NULL);

          INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name,\
                             university, created_by, created_at, last_updated)
          VALUES (6, true, NULL, true, 'Allgemeine Informationen', 'HS-KE', \
                  'Admin User', '2025-05-12 00:00:00', NULL);

          INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name, \
                             university, created_by, created_at, last_updated)
          VALUES (8, true, NULL, true, 'Architektur Prinzipien', 'HS-KE', \
                  'Admin User', '2025-05-12 00:00:00', NULL);

          INSERT INTO topic (lms_id, is_topic, parent_id, contains_le, name,\
                             university, created_by, created_at, last_updated)
          VALUES (9, true, NULL, true, 'Redundanz', 'HS-KE', 'Admin User', \
                  '2025-05-12 00:00:00', NULL);
    """
    cursor.execute(sql)

    # Create course_topic (which topic belongs to which course)
    sql = """
          INSERT INTO course_topic (course_id, topic_id) VALUES (1, 1);

          INSERT INTO course_topic (course_id, topic_id) VALUES (1, 2);

          INSERT INTO course_topic (course_id, topic_id) VALUES (2, 3);

          INSERT INTO course_topic (course_id, topic_id) VALUES (2, 4);

          INSERT INTO course_topic (course_id, topic_id) VALUES (2, 5);
    """
    cursor.execute(sql)

    # Create default learning path
    sql = """
          INSERT INTO default_learning_path (classification, position, \
                                             disabled, university)
          VALUES ('KÜ', 1, false, 'HS-KE');

          INSERT INTO default_learning_path (classification, position, \
                                             disabled, university)
          VALUES ('FO', 2, false, 'HS-KE');

          INSERT INTO default_learning_path (classification, position, \
                                             disabled, university)
          VALUES ('LZ', 3, false, 'HS-KE');

          INSERT INTO default_learning_path (classification, position, \
                                             disabled, university)
          VALUES ('EK', 4, false, 'HS-KE');

          INSERT INTO default_learning_path (classification, position, \
                                             disabled, university)
          VALUES ('AN', 5, false, 'HS-KE');

          INSERT INTO default_learning_path (classification, position, \
                                             disabled, university)
          VALUES ('ÜB', 6, false, 'HS-KE');

          INSERT INTO default_learning_path (classification, position, \
                                             disabled, university)
          VALUES ('AB', 7, false, 'HS-KE');

          INSERT INTO default_learning_path (classification, position, \
                                             disabled, university)
          VALUES ('BE', 8, false, 'HS-KE');

          INSERT INTO default_learning_path (classification, position, \
                                             disabled, university)
          VALUES ('SE', 9000, true, 'HS-KE');

          INSERT INTO default_learning_path (classification, position, \
                                             disabled, university)
          VALUES ('ZL', 9001, true, 'HS-KE');

          INSERT INTO default_learning_path (classification, position, \
                                             disabled, university)
          VALUES ('ZF', 9002, true, 'HS-KE');

          INSERT INTO default_learning_path (classification, position, \
                                             disabled, university)
          VALUES ('RQ', 9003, true, 'HS-KE');
    """
    cursor.execute(sql)

    # Create Student (course creators are also added to get learning paths)
    sql = """
          INSERT INTO student (user_id) VALUES (1);

          INSERT INTO student (user_id) VALUES (2);

          INSERT INTO student (user_id) VALUES (3);

          INSERT INTO student (user_id) VALUES (4);
    """
    cursor.execute(sql)

    # Create ILS Questionnaire ID
    sql = """
          INSERT INTO questionnaire_ils (student_id) VALUES (1);

          INSERT INTO questionnaire_ils (student_id) VALUES (2);

          INSERT INTO questionnaire_ils (student_id) VALUES (3);

          INSERT INTO questionnaire_ils (student_id) VALUES (4);
    """
    cursor.execute(sql)

    # Create ILS_input answers
    sql = """
          INSERT INTO ils_input_answers (questionnaire_ils_id, vv_1_f3, vv_2_f7, \
                                         vv_3_f11, vv_4_f15, vv_5_f19, vv_6_f23, \
                                         vv_7_f27, vv_8_f31, vv_9_f35, \
                                         vv_10_f39, vv_11_f43)
          VALUES (1, 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b');

          INSERT INTO ils_input_answers (questionnaire_ils_id, vv_1_f3, vv_2_f7, \
                                         vv_3_f11, vv_4_f15, vv_5_f19, vv_6_f23, \
                                         vv_7_f27, vv_8_f31, vv_9_f35, \
                                         vv_10_f39, vv_11_f43)
          VALUES (2, 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b');

          INSERT INTO ils_input_answers (questionnaire_ils_id, vv_1_f3, vv_2_f7, \
                                         vv_3_f11, vv_4_f15, vv_5_f19, vv_6_f23, \
                                         vv_7_f27, vv_8_f31, vv_9_f35, \
                                         vv_10_f39, vv_11_f43)
          VALUES (3, 'a', 'b', 'a', 'b', 'a', 'a', 'a', 'b', 'a', 'a', 'b');

          INSERT INTO ils_input_answers (questionnaire_ils_id, vv_1_f3, vv_2_f7, \
                                         vv_3_f11, vv_4_f15, vv_5_f19, vv_6_f23, \
                                         vv_7_f27, vv_8_f31, vv_9_f35, \
                                         vv_10_f39, vv_11_f43)
          VALUES (4, 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'a', 'a', 'a');
    """
    cursor.execute(sql)

    # Create ILS_perception answers
    sql = """
          INSERT INTO ils_perception_answers (questionnaire_ils_id, si_1_f2,
                                              si_2_f6, si_3_f10, si_4_f14, si_5_f18, \
                                              si_6_f22, si_7_f26, si_8_f30, \
                                              si_9_f34, si_10_f38, si_11_f42)
          VALUES (1, 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a');

          INSERT INTO ils_perception_answers (questionnaire_ils_id, si_1_f2,
                                              si_2_f6, si_3_f10, si_4_f14, si_5_f18, \
                                              si_6_f22, si_7_f26, si_8_f30, \
                                              si_9_f34, si_10_f38, si_11_f42)
          VALUES (2, 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a');

          INSERT INTO ils_perception_answers (questionnaire_ils_id, si_1_f2,
                                              si_2_f6, si_3_f10, si_4_f14, si_5_f18, \
                                              si_6_f22, si_7_f26, si_8_f30, \
                                              si_9_f34, si_10_f38, si_11_f42)
          VALUES (3, 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a', 'b', 'a');

          INSERT INTO ils_perception_answers (questionnaire_ils_id, si_1_f2,
                                              si_2_f6, si_3_f10, si_4_f14, si_5_f18, \
                                              si_6_f22, si_7_f26, si_8_f30, \
                                              si_9_f34, si_10_f38, si_11_f42)
          VALUES (4, 'a', 'b', 'b', 'a', 'b', 'b', 'b', 'b', 'b', 'a', 'a');
    """
    cursor.execute(sql)

    # Create ILS_processing answers
    sql = """
          INSERT INTO ils_processing_answers (questionnaire_ils_id, ar_1_f1, \
                                              ar_2_f5, ar_3_f9, ar_4_f13, ar_5_f17, \
                                              ar_6_f21, ar_7_f25, ar_8_f29, \
                                              ar_9_f33, ar_10_f37, ar_11_f41)
          VALUES (1, 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a');

          INSERT INTO ils_processing_answers (questionnaire_ils_id, ar_1_f1, \
                                              ar_2_f5, ar_3_f9, ar_4_f13, ar_5_f17, \
                                              ar_6_f21, ar_7_f25, ar_8_f29, \
                                              ar_9_f33, ar_10_f37, ar_11_f41)
          VALUES (2, 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a');

          INSERT INTO ils_processing_answers (questionnaire_ils_id, ar_1_f1, \
                                              ar_2_f5, ar_3_f9, ar_4_f13, ar_5_f17, \
                                              ar_6_f21, ar_7_f25, ar_8_f29, \
                                              ar_9_f33, ar_10_f37, ar_11_f41)
          VALUES (3, 'a', 'a', 'b', 'b', 'b', 'a', 'b', 'a', 'a', 'b', 'a');

          INSERT INTO ils_processing_answers (questionnaire_ils_id, ar_1_f1, \
                                              ar_2_f5, ar_3_f9, ar_4_f13, ar_5_f17, \
                                              ar_6_f21, ar_7_f25, ar_8_f29, \
                                              ar_9_f33, ar_10_f37, ar_11_f41)
          VALUES (4, 'a', 'a', 'a', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a');
    """
    cursor.execute(sql)

    # Create ILS_understanding answers
    sql = """
          INSERT INTO ils_understanding_answers (questionnaire_ils_id, sg_1_f4, \
                                                 sg_2_f8, sg_3_f12, sg_4_f16, sg_5_f20,\
                                                 sg_6_f24, sg_7_f28, sg_8_f32, \
                                                 sg_9_f36, sg_10_f40, sg_11_f44)
          VALUES (1, 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b');

          INSERT INTO ils_understanding_answers (questionnaire_ils_id, sg_1_f4, \
                                                 sg_2_f8, sg_3_f12, sg_4_f16, sg_5_f20,\
                                                 sg_6_f24, sg_7_f28, sg_8_f32, \
                                                 sg_9_f36, sg_10_f40, sg_11_f44)
          VALUES (2, 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b');

          INSERT INTO ils_understanding_answers (questionnaire_ils_id, sg_1_f4, \
                                                 sg_2_f8, sg_3_f12, sg_4_f16, sg_5_f20,\
                                                 sg_6_f24, sg_7_f28, sg_8_f32, \
                                                 sg_9_f36, sg_10_f40, sg_11_f44)
          VALUES (3, 'a', 'b', 'b', 'a', 'a', 'a', 'b', 'b', 'a', 'a', 'a');

          INSERT INTO ils_understanding_answers (questionnaire_ils_id, sg_1_f4, \
                                                 sg_2_f8, sg_3_f12, sg_4_f16, sg_5_f20,\
                                                 sg_6_f24, sg_7_f28, sg_8_f32, \
                                                 sg_9_f36, sg_10_f40, sg_11_f44)
          VALUES (4, 'a', 'a', 'b', 'b', 'a', 'b', 'b', 'a', 'b', 'a', 'a');
    """
    cursor.execute(sql)

    # Create learning characteristics
    sql = """
          INSERT INTO learning_characteristics (student_id) VALUES (1);
          INSERT INTO learning_characteristics (student_id) VALUES (2);
          INSERT INTO learning_characteristics (student_id) VALUES (3);
          INSERT INTO learning_characteristics (student_id) VALUES (4);
    """
    cursor.execute(sql)

    # Create knowledge id´s
    sql = """
          INSERT INTO knowledge (characteristic_id) VALUES (1);
          INSERT INTO knowledge (characteristic_id) VALUES (2);
          INSERT INTO knowledge (characteristic_id) VALUES (3);
          INSERT INTO knowledge (characteristic_id) VALUES (4);
    """
    cursor.execute(sql)

    # Create learning analytics id´s
    sql = """
          INSERT INTO learning_analytics (characteristic_id) VALUES (1);
          INSERT INTO learning_analytics (characteristic_id) VALUES (2);
          INSERT INTO learning_analytics (characteristic_id) VALUES (3);
          INSERT INTO learning_analytics (characteristic_id) VALUES (4);
    """
    cursor.execute(sql)

    # Create Learning Elements
    sql = """
          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, \
                                        last_updated)
          VALUES (3, 'h5pactivity', 'EK', 'Adapter Muster', 'HS-KE', 'Admin User', \
                  '2025-05-09 00:00:00', NULL);

          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, \
                                        last_updated)
          VALUES (12, 'h5pactivity', 'SE', 'Fassade Muster', 'HS-KE', 'Admin User', \
                  '2025-05-09 00:00:00', NULL);

          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, \
                                        last_updated)
          VALUES (8, 'h5pactivity', 'EK', 'Halstead Metrik', 'HS-KE', 'Admin User', \
                  '2025-05-12 00:00:00', NULL);

          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, \
                                        last_updated)
          VALUES (10, 'h5pactivity', 'BE', 'Lines of Code', 'HS-KE', 'Admin User', \
                  '2025-05-12 00:00:00', NULL);

          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                       university, created_by, created_at, \
                                        last_updated)
          VALUES (9, 'h5pactivity', 'SE', 'Zyklomatische Komplexität', 'HS-KE', \
                  'Admin User', '2025-05-12 00:00:00', NULL);

          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, \
                                        last_updated)
          VALUES (5, 'forum', 'FO', 'Definition Software Architektur', 'HS-KE', \
                  'Admin User', '2025-05-12 00:00:00', NULL);

          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, \
                                        last_updated)
          VALUES (27, 'h5pactivity', 'BE', 'Funktionale Anforderungen', 'HS-KE', \
                  'Admin User', '2025-05-12 00:00:00', NULL);

          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, \
                                        last_updated)
          VALUES (45, 'h5pactivity', 'BE', 'Nichtfunktionale Anforderungen', 'HS-KE', \
                  'Admin User', '2025-05-12 00:00:00', NULL);

          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, \
                                        last_updated)
          VALUES (11, 'h5pactivity', 'LZ', 'Hohe Kohäsion', 'HS-KE', 'Admin User', \
                  '2025-05-12 00:00:00', NULL);

          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, \
                                        last_updated)
          VALUES (17, 'h5pactivity', 'ÜB', 'Open closed principle', 'HS-KE', \
                  'Admin User', '2025-05-12 00:00:00', NULL);

          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at, \
                                        last_updated)
          VALUES (21, 'h5pactivity', 'AN', 'Standby-Redundanz', 'HS-KE', \
                  'Admin User', '2025-05-12 00:00:00', NULL);

          INSERT INTO learning_element (lms_id, activity_type, classification, name, \
                                        university, created_by, created_at,\
                                        last_updated)
          VALUES (25, 'h5pactivity', 'ZF', 'Heiße Redundanz', 'HS-KE', 'Admin User', \
                  '2025-05-12 00:00:00', NULL);
    """
    cursor.execute(sql)

    # Create learning paths for each user
    sql = """
          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (1, 1, 'default', 1, '2025-05-09 12:43:26+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (2, 1, 'default', 1, '2025-05-09 12:44:03+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (1, 1, 'aco', 2, '2025-05-12 10:35:02+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (2, 1, 'aco', 2, '2025-05-12 10:35:02+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (1, 2, 'ga', 3, '2025-05-12 10:36:25+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (2, 2, 'ga', 3, '2025-05-12 10:36:26+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (1, 2, 'graf', 4, '2025-05-12 10:36:43+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (2, 2, 'graf', 4, '2025-05-12 10:36:44+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (1, 2, 'aco', 5, '2025-05-12 10:37:01+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (2, 2, 'aco', 5, '2025-05-12 10:37:01+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (3, 1, 'default', 1, '2025-05-12 10:50:18+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (3, 1, 'aco', 2, '2025-05-12 10:50:18+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (3, 2, 'ga', 3, '2025-05-12 10:50:19+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (3, 2, 'graf', 4, '2025-05-12 10:50:19+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (3, 2, 'aco', 5, '2025-05-12 10:50:19+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (4, 1, 'default', 1, '2025-05-12 10:54:52+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (4, 1, 'aco', 2, '2025-05-12 10:54:52+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (4, 2, 'ga', 3, '2025-05-12 10:54:52+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (4, 2, 'graf', 4, '2025-05-12 10:54:53+02');

          INSERT INTO learning_path (student_id, course_id, based_on, \
                                     topic_id, calculated_on)
          VALUES (4, 2, 'aco', 5, '2025-05-12 10:54:53+02');
    """
    cursor.execute(sql)

    # Create learning path learning elements
    # (which learning element belongs to which learning path)
    sql = """
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (1, 1, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (2, 1, true, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (1, 2, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (2, 2, true, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (3, 3, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (4, 3, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (5, 3, false, 3);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (3, 4, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (4, 4, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (5, 4, false, 3);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (6, 5, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (8, 5, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (7, 5, false, 3);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (6, 6, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (8, 6, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (7, 6, false, 3);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (10, 7, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (9, 7, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (10, 8, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (9, 8, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (11, 9, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (12, 9, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (11, 10, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (12, 10, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (1, 11, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (2, 11, true, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (3, 12, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (4, 12, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (5, 12, false, 3);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (8, 13, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (7, 13, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (6, 13, false, 3);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (10, 14, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (9, 14, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (11, 15, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (12, 15, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (1, 16, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (2, 16, true, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (3, 17, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (4, 17, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (5, 17, false, 3);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (8, 18, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (6, 18, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (7, 18, false, 3);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (10, 19, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (9, 19, false, 2);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (11, 20, true, 1);
          INSERT INTO learning_path_learning_element (learning_element_id, \
                                                      learning_path_id, \
                                                      position) \
          VALUES (12, 20, false, 2);
    """
    cursor.execute(sql)

    # Create learning path learning element algorithm
    # (which algorithm belongs to which learning path)
    sql = """
          INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)\
          VALUES (1, 1);
          INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)\
          VALUES (2, 2);
          INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)\
          VALUES (3, 3);
          INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)\
          VALUES (4, 4);
          INSERT INTO learning_path_learning_element_algorithm (topic_id, algorithm_id)\
          VALUES (5, 2);
    """
    cursor.execute(sql)

    # Create learning strategy
    sql = """
          INSERT INTO learning_strategy (characteristic_id, cogn_str, org, elab, \
                                         crit_rev, rep, metacogn_str, goal_plan, con,\
                                         reg, int_res_mng_str, \
                                         att, eff, time, ext_res_mng_str, lrn_w_cls, \
                                         lit_res, lrn_env)
          VALUES (1, 1.33, 2.33, 3.33, 4.33, 1.33, 2.33, 3.33, 4.33, 1.33, 2.33, \
                  3.33, 4.33, 1.33, 2.33, 3.33, 4.33, 1.33);

          INSERT INTO learning_strategy (characteristic_id, cogn_str, org, elab, \
                                         crit_rev, rep, metacogn_str, goal_plan, con, \
                                         reg, int_res_mng_str, \
                                         att, eff, time, ext_res_mng_str, lrn_w_cls, \
                                         lit_res, lrn_env)
          VALUES (2, 1.67, 2.67, 3.74, 4.84, 2.45, 2.88, 3.78, 4.77, 1.48, 2.88, \
                  3.03, 4.79, 1.50, 2.78, 3.99, 4.04, 1.79);

          INSERT INTO learning_strategy (characteristic_id, cogn_str, org, elab, \
                                         crit_rev, rep, metacogn_str, goal_plan, con, \
                                         reg, int_res_mng_str, \
                                         att, eff, time, ext_res_mng_str, lrn_w_cls, \
                                         lit_res, lrn_env)
          VALUES (3, 4.67, 3.67, 2.74, 1.84, 2.45, 4.88, 1.78, 1.77, 5.00, 3.88, \
                  3.03, 4.79, 1.50, 1.78, 2.99, 2.04, 1.79);

          INSERT INTO learning_strategy (characteristic_id, cogn_str, org, elab, \
                                         crit_rev, rep, metacogn_str, goal_plan, con, \
                                         reg, int_res_mng_str, \
                                         att, eff, time, ext_res_mng_str, lrn_w_cls, \
                                         lit_res, lrn_env)
          VALUES (4, 4.67, 3.67, 2.74, 1.84, 2.45, 4.88, 1.78, 1.77, 5.00, 3.88, \
              3.03, 4.79, 1.50, 1.78, 2.99, 2.04, 1.79);
    """
    cursor.execute(sql)

    # Create learning style
    sql = """
          INSERT INTO learning_style (characteristic_id, perception_dimension, \
                                      perception_value, input_dimension, input_value, \
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value) \
          VALUES (1, 'sns', 11, 'vrb', 11, 'act', 11, 'glo', 11);

          INSERT INTO learning_style (characteristic_id, perception_dimension, \
                                      perception_value, input_dimension, input_value, \
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value) \
          VALUES (2, 'sns', 11, 'vrb', 11, 'act', 11, 'glo', 11);

          INSERT INTO learning_style (characteristic_id, perception_dimension, \
                                      perception_value, input_dimension, input_value, \
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value) \
          VALUES (3, 'int', 7, 'vis', 3, 'act', 1, 'seq', 3);

          INSERT INTO learning_style (characteristic_id, perception_dimension, \
                                      perception_value, input_dimension, input_value, \
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value) \
          VALUES (4, 'int', 3, 'vis', 7, 'act', 7, 'seq', 1);
    """
    cursor.execute(sql)

    # Create settings
    sql = """
          INSERT INTO settings (user_id, theme, pswd) VALUES (1, 'Standard', NULL);
          INSERT INTO settings (user_id, theme, pswd) VALUES (2, 'Standard', NULL);
          INSERT INTO settings (user_id, theme, pswd) VALUES (3, 'Standard', NULL);
          INSERT INTO settings (user_id, theme, pswd) VALUES (4, 'Standard', NULL);
    """
    cursor.execute(sql)

    # Add students to courses
    sql = """
          INSERT INTO student_course (student_id, course_id, perception_dimension, \
                                      perception_value, input_dimension, input_value, \
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value)
          VALUES (1, 1, 'sns', 11, 'vrb', 11, 'act', 11, 'glo', 11);

          INSERT INTO student_course (student_id, course_id, perception_dimension, \
                                      perception_value, input_dimension, input_value,\
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value)
          VALUES (2, 1, 'sns', 11, 'vrb', 11, 'act', 11, 'glo', 11);

          INSERT INTO student_course (student_id, course_id, perception_dimension, \
                                      perception_value, input_dimension, input_value,\
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value)
          VALUES (1, 2, 'sns', 11, 'vrb', 11, 'act', 11, 'glo', 11);

          INSERT INTO student_course (student_id, course_id, perception_dimension, \
                                      perception_value, input_dimension, input_value,\
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value)
          VALUES (2, 2, 'sns', 11, 'vrb', 11, 'act', 11, 'glo', 11);

          INSERT INTO student_course (student_id, course_id, perception_dimension, \
                                      perception_value, input_dimension, input_value, \
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value)
          VALUES (3, 1, 'sns', 0, 'vrb', 0, 'act', 0, 'seq', 0);

          INSERT INTO student_course (student_id, course_id, perception_dimension, \
                                      perception_value, input_dimension, input_value, \
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value)
          VALUES (3, 2, 'sns', 0, 'vrb', 0, 'act', 0, 'seq', 0);

          INSERT INTO student_course (student_id, course_id, perception_dimension, \
                                      perception_value, input_dimension, input_value, \
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value)
          VALUES (4, 1, 'sns', 0, 'vrb', 0, 'act', 0, 'seq', 0);

          INSERT INTO student_course (student_id, course_id, perception_dimension, \
                                      perception_value, input_dimension, input_value,\
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value)
          VALUES (4, 2, 'sns', 0, 'vrb', 0, 'act', 0, 'seq', 0);

          INSERT INTO student_course (student_id, course_id, perception_dimension, \
                                      perception_value, input_dimension, input_value,\
                                      processing_dimension, processing_value,\
                                      understanding_dimension, understanding_value)
          VALUES (1, 3, 'sns', 1, 'vrb', 1, 'act', 9,'seq', 9);

          INSERT INTO student_course (student_id, course_id, perception_dimension, \
                                      perception_value, input_dimension, input_value, \
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value)
          VALUES (2, 3, 'sns', 1, 'vrb', 1, 'act', 9,'seq', 9);

          INSERT INTO student_course (student_id, course_id, perception_dimension, \
                                      perception_value, input_dimension, input_value, \
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value)
          VALUES (3, 3, 'sns', 0, 'vrb', 0, 'act', 0,'seq', 0);

          INSERT INTO student_course (student_id, course_id, perception_dimension, \
                                      perception_value, input_dimension, input_value, \
                                      processing_dimension, processing_value, \
                                      understanding_dimension, understanding_value)
          VALUES (4, 3, 'sns', 0, 'vrb', 0, 'act', 0,'seq', 0);
    """
    cursor.execute(sql)

    # Add students to learning elements
    sql = """
          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 1, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 2, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 1, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 2, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 1, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 2, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 3, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 3, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 4, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 4, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 5, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 5, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 1, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 2, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 3, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 4, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 5, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 1, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 2, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 3, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 4, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 5, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 6, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 6, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 7, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 7, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 8, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 8, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 6, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 7, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 8, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 6, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 7, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 8, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 9, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 10, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 9, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 10, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 6, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 7, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 8, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
           done, done_at)
          VALUES (1, 9, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
           done, done_at)
          VALUES (1, 10, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 6, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 7, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 8, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 9, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
           done, done_at)
          VALUES (2, 10, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 11, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 11, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
           done, done_at)
          VALUES (1, 12, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
           done, done_at)
          VALUES (2, 12, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
           done, done_at)
          VALUES (1, 6, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
           done, done_at)
          VALUES (1, 7, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
           done, done_at)
          VALUES (1, 8, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
           done, done_at)
          VALUES (1, 9, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 10, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 11, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (1, 12, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 6, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 7, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 8, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 9, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 10, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 11, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (2, 12, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (3, 1, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (3, 2, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
           done, done_at)
          VALUES (3, 3, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (3, 4, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (3, 5, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (3, 6, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (3, 7, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (3, 8, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
          done, done_at)
          VALUES (3, 9, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (3, 10, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
          done, done_at)
          VALUES (3, 11, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
          done, done_at)
          VALUES (3, 12, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
          done, done_at)
          VALUES (4, 1, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
          done, done_at)
          VALUES (4, 2, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
          done, done_at)
          VALUES (4, 3, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (4, 4, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
          done, done_at)
          VALUES (4, 5, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id, \
          done, done_at)
          VALUES (4, 6, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
          done, done_at)
          VALUES (4, 7, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
          done, done_at)
          VALUES (4, 8, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
          done, done_at)
          VALUES (4, 9, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
          done, done_at)
          VALUES (4, 10, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
          done, done_at)
          VALUES (4, 11, false, NULL);

          INSERT INTO student_learning_element (student_id, learning_element_id,\
          done, done_at)
          VALUES (4, 12, false, NULL);
    """
    cursor.execute(sql)

    # create student learning path algorithms
    sql = """
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id, \
                                                                        algorithm_id)\
          VALUES (1, 1, 1);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (1, 1, 1);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (2, 1, 1);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (1, 2, 2);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (2, 2, 2);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (1, 1, 1);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (1, 2, 2);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (2, 1, 1);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (2, 2, 2);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (1, 3, 3);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (2, 3, 3);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (1, 3, 3);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (2, 3, 3);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (1, 4, 4);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (2, 4, 4);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (1, 3, 3);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id, \
                                                                        algorithm_id)\
          VALUES (1, 4, 4);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (2, 3, 3);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (2, 4, 4);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (1, 5, 2);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (2, 5, 2);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (1, 3, 3);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (1, 4, 4);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (1, 5, 2);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (2, 3, 3);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (2, 4, 4);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (2, 5, 2);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (3, 1, 1);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (3, 2, 2);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (3, 3, 3);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                        algorithm_id)\
          VALUES (3, 4, 4);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                         algorithm_id)\
          VALUES (3, 5, 2);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                         algorithm_id)\
          VALUES (4, 1, 1);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                         algorithm_id)\
          VALUES (4, 2, 2);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                         algorithm_id)\
          VALUES (4, 3, 3);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                         algorithm_id)\
          VALUES (4, 4, 4);
          INSERT INTO student_learning_path_learning_element_algorithm (student_id,\
                                                                        topic_id,\
                                                                         algorithm_id)\
          VALUES (4, 5, 2);
    """
    cursor.execute(sql)

    # Add students to topics
    sql = """
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (1, 1, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (2, 1, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (1, 1, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (1, 2, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (2, 1, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (2, 2, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (1, 3, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (2, 3, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (1, 3, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (1, 4, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (2, 3, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (2, 4, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (1, 3, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (1, 4, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (1, 5, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (2, 3, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (2, 4, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (2, 5, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (3, 1, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (3, 2, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (3, 3, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (3, 4, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (3, 5, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (4, 1, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (4, 2, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (4, 3, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (4, 4, false, NULL);
          INSERT INTO student_topic (student_id, topic_id, done, \
                                     done_at) VALUES (4, 5, false, NULL);
    """
    cursor.execute(sql)

    # Define which elements are in which topics
    sql = """
          INSERT INTO topic_learning_element (topic_id, \
                                              learning_element_id) VALUES (1, 1);
          INSERT INTO topic_learning_element (topic_id, \
                                              learning_element_id) VALUES (1, 2);
          INSERT INTO topic_learning_element (topic_id, \
                                              learning_element_id) VALUES (2, 3);
          INSERT INTO topic_learning_element (topic_id, \
                                              learning_element_id) VALUES (2, 4);
          INSERT INTO topic_learning_element (topic_id, \
                                              learning_element_id) VALUES (2, 5);
          INSERT INTO topic_learning_element (topic_id, \
                                              learning_element_id) VALUES (3, 6);
          INSERT INTO topic_learning_element (topic_id, \
                                              learning_element_id) VALUES (3, 7);
          INSERT INTO topic_learning_element (topic_id, \
                                              learning_element_id) VALUES (3, 8);
          INSERT INTO topic_learning_element (topic_id, \
                                              learning_element_id) VALUES (4, 9);
          INSERT INTO topic_learning_element (topic_id, \
                                              learning_element_id) VALUES (4, 10);
          INSERT INTO topic_learning_element (topic_id, \
                                              learning_element_id) VALUES (5, 11);
          INSERT INTO topic_learning_element (topic_id, \
                                              learning_element_id) VALUES (5, 12);
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
