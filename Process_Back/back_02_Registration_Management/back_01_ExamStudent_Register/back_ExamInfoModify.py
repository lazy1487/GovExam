from publicUseFunction import importPackage, dbConnection
back_ExamInfoModify = importPackage.Blueprint(
    'back_ExamInfoModify', __name__)
back_ExamInfoModify.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)

@back_ExamInfoModify.route('/backExamInfoModify', methods=['GET', 'POST'])
def backExamInfoModify():
    conn = pool.getconn()

    ExamStyleID = str(importPackage.request.args.get('ExamStyleID'))
    ExamTitle = str(importPackage.request.args.get('ExamTitle'))
    Listresult = []  # Initialize Listresult here
    try:
        cursor = conn.cursor()
        # ==========抓取所有考試資訊資料========== #
        cursor.execute(
            """ Select * from "back_ExamSetting" Where "inputExamStyleID"= %s and "inputExamTitle"=%s """,(ExamStyleID,ExamTitle,))
        result = cursor.fetchall()

        # ==========抓取所有考試類別資料========== #
        cursor.execute(
            """ Select "inputExamStyleID","inputExamStyle" from "back_ExamStyleSetting" """)
        Listresult = cursor.fetchall()

    except Exception as e:
        result = None
        print('Error')
    finally:
        cursor.close()
        pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamInfoModify.html', result=result, Listresult=Listresult)
