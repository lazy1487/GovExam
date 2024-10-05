from publicUseFunction import importPackage, dbConnection
back_ExamInfoSetting = importPackage.Blueprint(
    'back_ExamInfoSetting', __name__)
back_ExamInfoSetting.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_ExamInfoSetting.route('/backExamInfoSetting', methods=['GET', 'POST'])
def backExamRegister():

    user = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    print(user_name)

    conn = pool.getconn()

    try:
        cursor = conn.cursor()
        # ==========抓取所有考試資訊資料========== #
        cursor.execute(
            """ Select * from "back_ExamSetting" """)
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
        return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamInfoSetting.html', result=result, Listresult=Listresult, user_name=user_name)
