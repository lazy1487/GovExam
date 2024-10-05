from publicUseFunction import importPackage, dbConnection
back_ExamStyleModify = importPackage.Blueprint(
    'back_ExamStyleModify', __name__)
back_ExamStyleModify.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

@back_ExamStyleModify.route('/backExamStyleModify', methods=['GET', 'POST'])
def backExamStyleModify():

    user = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()
    
    inputExamStyleID = str(importPackage.request.args.get('inputExamStyleID'))

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
    else:
        try:
            with conn.cursor() as cur:
                cur.execute("""SELECT * FROM "back_ExamStyleSetting" where "inputExamStyleID"=%s """,(inputExamStyleID,))
                result = cur.fetchall()
        except:
            result = None
            print('Error')
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamStyleModify.html', result=result,Handler=user,DateTime=formatted_time)
    

   