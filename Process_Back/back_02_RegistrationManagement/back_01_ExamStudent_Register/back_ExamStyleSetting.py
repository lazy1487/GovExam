from publicUseFunction import importPackage, dbConnection
back_ExamStyleSetting = importPackage.Blueprint(
    'back_ExamStyleSetting', __name__)
back_ExamStyleSetting.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

@back_ExamStyleSetting.route('/backExamStyleSetting', methods=['GET', 'POST'])
def backExamRegister():
    
    conn = pool.getconn()

    if importPackage.request.method == "POST":
        inputExamStyle = importPackage.request.form['inputExamStyle']
        
        try:
            with conn.cursor() as cursor:
                if inputExamStyle != '':
                    with conn.cursor() as cur:
                        cur.execute("""
                            INSERT INTO "back_ExamStyleSetting" (
                            "inputExamStyle", "isUse") VALUES (%s, %s)""",
                                    (inputExamStyle, "false"))
                        conn.commit()
        except Exception as e:
            result=None
            print('Error')
        finally:
            cursor.close()
            pool.putconn(conn)
    
    try:
        with conn.cursor() as cur:
            cur.execute("""SELECT "inputExamStyle" FROM "back_ExamStyleSetting" """)
            result = cur.fetchall()
    except Exception as e:
        result=None
        print('Error')


    return importPackage.render_template('後台網頁/back_02_Registration _Management/back_01_ExamStudent_Register/back_ExamStyleSetting.html', result=result)

@back_ExamStyleSetting.route('/backExamRegisterDelete', methods=['GET', 'POST'])
def backExamRegisterDelete():
    conn = pool.getconn()
    if importPackage.request.method == "POST":
        inputExamStyle = importPackage.request.form.get('hiddeninputExamStyle')
        print(inputExamStyle)
        return importPackage.redirect(importPackage.url_for('back_ExamStyleSetting.backExamRegister'))
    else:
        try:
            with conn.cursor() as cursor:
                cursor.execute("""SELECT "inputExamStyle" FROM "back_ExamStyleSetting" """)
                result = cursor.fetchall()
        except Exception as e:
            result=None
            print('Error')
        return importPackage.render_template('後台網頁/back_02_Registration _Management/back_01_ExamStudent_Register/back_ExamStyleSetting.html',Resetresult=result)