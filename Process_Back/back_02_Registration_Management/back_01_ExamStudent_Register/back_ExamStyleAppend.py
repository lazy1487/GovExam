from publicUseFunction import importPackage, dbConnection
back_ExamStyleAppend = importPackage.Blueprint(
    'back_ExamStyleAppend', __name__)
back_ExamStyleAppend.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

@back_ExamStyleAppend.route('/backExamStyleAppend', methods=['GET', 'POST'])
def backExamStyleAppend():

    PublicUseBackName = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()

    if importPackage.request.method == "POST":
        hiddeninputExamStyleID = importPackage.request.form['hiddeninputExamStyleID']
        hiddeninputExamStyle = importPackage.request.form['hiddeninputExamStyle']
        hiddeninputExamStyleDes = importPackage.request.form['hiddeninputExamStyleDes']
        hiddeninputExamStyleIsUsed = importPackage.request.form['hiddeninputExamStyleIsUsed']
        hiddeninputExamStyleStartTime = importPackage.request.form['hiddeninputExamStyleStartTime']
        hiddeninputExamStyleEndTime = importPackage.request.form['hiddeninputExamStyleEndTime']


        cursor = conn.cursor()
        cursor.execute(
            """ INSERT INTO "back_ExamStyleSetting" ("inputExamStyleID","inputExamStyle","inputExamStyleDes","inputExamStyleIsUsed","inputExamStyleStartTime","inputExamStyleEndTime")
                VALUES (%s,%s,%s,%s,%s,%s) """, (hiddeninputExamStyleID, hiddeninputExamStyle, hiddeninputExamStyleDes, hiddeninputExamStyleIsUsed, hiddeninputExamStyleStartTime, hiddeninputExamStyleEndTime))
        conn.commit()
        conn.close()

    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamStyleAppend.html', Handler=PublicUseBackName, DateTime=formatted_time)