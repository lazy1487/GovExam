from publicUseFunction import importPackage, dbConnection
back_ExamIndex = importPackage.Blueprint(
    'back_ExamIndex', __name__)
back_ExamIndex.secret_key = 'abc'
conn = importPackage.conn
pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_ExamIndex.route('/backExamIndex', methods=['GET', 'POST'])
def backExamInfo():

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamIndex.html', user_name=user_name)
