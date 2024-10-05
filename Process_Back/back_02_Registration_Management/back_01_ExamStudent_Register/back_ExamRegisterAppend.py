from publicUseFunction import importPackage, dbConnection
back_ExamRegisterAppend = importPackage.Blueprint(
    'back_ExamRegisterAppend', __name__)
back_ExamRegisterAppend.secret_key = 'abc'
conn = importPackage.conn
pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


current_time = importPackage.datetime.datetime.now()
formatted_time = current_time.strftime("%Y/%m/%d")


@back_ExamRegisterAppend.route('/backExamRegisterAppend', methods=['GET', 'POST'])
def backExamRegisterAppend():

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    try:
        print()
    except Exception as e:
        result = None
        print('Error')
    finally:
        # cursor.close()
        # pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamRegisterAppend.html', user_id=user_id, user_name=user_name)


@back_ExamRegisterAppend.route('/back_ExamRegisterAppend_EdccationSearch', methods=['POST'])
def backExamRegisterAppendEdccationSearch():
    school_areaCode = importPackage.request.form.get('school_areaCode')
    school_StyleCode = importPackage.request.form.get('school_StyleCode')
    try:
        print(school_areaCode, school_StyleCode)
        cursor = conn.cursor()
        cursor.execute(
            """ SELECT "school_Name","school_DepaName","school_CityPostalCode", "school_City", "school_CityArea", "school_Address" FROM other."other_ShcoolData" where "school_areaCode"=%s and "school_StyleCode"=%s """, (school_areaCode, school_StyleCode))
        result = cursor.fetchall()

    except Exception as e:
        result = None
        print('Error')
    finally:
        cursor.close()
        # pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamRegisterAppend.html', result=result)
