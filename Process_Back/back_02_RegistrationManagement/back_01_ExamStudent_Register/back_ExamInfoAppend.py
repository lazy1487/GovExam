from publicUseFunction import importPackage, dbConnection
back_ExamInfoAppend = importPackage.Blueprint(
    'back_ExamInfoAppend', __name__)
back_ExamInfoAppend.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

@back_ExamInfoAppend.route('/backExamInfoAppend', methods=['GET', 'POST'])
def backExamRegister():
    conn = pool.getconn()

    try:
        cursor = conn.cursor()
        cursor.execute(
            """ Select "inputExamStyle" from "back_ExamStyleSetting" """)
        result = cursor.fetchall()
    except Exception as e:
        result = None
        print('Error')
    finally:
        cursor.close()
        pool.putconn(conn)
        
    return importPackage.render_template('後台網頁/back_02_Registration _Management/back_01_ExamStudent_Register/back_ExamInfoAppend.html',result=result)
