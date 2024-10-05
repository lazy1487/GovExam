from publicUseFunction import importPackage, dbConnection
back_ExamInfoSort = importPackage.Blueprint(
    'back_ExamInfoSort', __name__)
back_ExamInfoSort.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_ExamInfoSort.route('/backExamInfoSort', methods=['GET', 'POST'])
def backExamInfoSort():
    conn = pool.getconn()
    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamInfoSort.html')
