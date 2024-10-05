from publicUseFunction import importPackage, dbConnection
back_ExamStyleSort = importPackage.Blueprint(
    'back_ExamStyleSort', __name__)
back_ExamStyleSort.secret_key = 'abc'
conn = importPackage.conn

@back_ExamStyleSort.route('/backExamStyleSort', methods=['GET', 'POST'])
def backExamRegister():
    PublicUseBackName = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    with conn.cursor() as cursor:
        cursor.execute("""SELECT "inputExamStyleID","inputExamStyle","inputexamcreatesort" FROM "back_ExamStyleSetting" """)
        result = cursor.fetchall()
    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamStyleSort.html',result=result,Handler=PublicUseBackName,DateTime=formatted_time)
