from publicUseFunction import importPackage, dbConnection
back_ExamInfoImport = importPackage.Blueprint(
    'back_ExamInfoImport', __name__)
back_ExamInfoImport.secret_key = 'abc'
conn = importPackage.conn
pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_ExamInfoImport.route('/backExamInfoImport', methods=['GET', 'POST'])
def backExamInfo():
    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamInfoImport.html')
