from publicUseFunction import importPackage, dbConnection
back_ExamStyleImport = importPackage.Blueprint(
    'back_ExamStyleImport', __name__)
back_ExamStyleImport.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_ExamStyleImport.route('/backExamStyleImport', methods=['GET', 'POST'])
def backExamStyleImport():
    user_id = importPackage.session.get("user_id")
    user_name = importPackage.session.get("user_name")
    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamStyleImport.html',user_name=user_name)
