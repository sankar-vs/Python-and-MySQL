'''
@Author: Sankar
@Date: 2021-04-24 06:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-26 09:38:09
@Title : Stored Procedures
'''
from SQL_Connect import CRUD
from log import logger

class StoredProcedures():
    '''
    Class:
        StoredProcedures
    Description:
        To Call Stored Procedure From the Database.
    Functions:
        call_get_merit_student()
        call_get_student_by_limit()
        call_max_display_marks()
        call_display_marks()
        show_stored_procedures()
        call_display_students_by_limit()
    Variable:
        None
    '''
    def __init__(self):
        self.connect = CRUD()

    def call_get_merit_student(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            cursor.callproc('get_merit_student')

            for result in cursor.stored_results():
                for i in result.fetchall():
                    logger.info(i)

        except:
            logger.exception("Call Procedure Aborted")

    def call_get_student_by_limit(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            cursor.callproc('get_student',[4,])

            for result in cursor.stored_results():
                for i in result.fetchall():
                    logger.info(i)

        except:
            logger.exception("Call Procedure Aborted")

    def call_max_display_marks(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            result_arg = cursor.callproc('display_max_mark',[1])

            logger.info(result_arg[0])

        except:
            logger.exception("Call Procedure Aborted")

    def call_display_marks(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            result_arg = cursor.callproc('display_marks',[3])

            logger.info(result_arg[0])

        except:
            logger.exception("Call Procedure Aborted")

    def show_stored_procedures(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            cursor.execute("SHOW PROCEDURE STATUS WHERE db = '{}'".format(self.connect._CRUD__database_name))

            result = cursor.fetchall()

            for i in result:
                logger.info(i)

        except:
            logger.exception("Show Procedure Aborted")

    def call_display_students_by_limit(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            result_arg = cursor.callproc('display_students_by_limit',[1,5,92])
            
            for result in cursor.stored_results():
                for i in result.fetchall():
                    logger.info(i)

            logger.info(result_arg[2])

        except:
            logger.exception("Show Procedure Aborted")
    