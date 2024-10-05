from publicUseFunction import importPackage, dbConnection
back_AgencyInfoIndex = importPackage.Blueprint(
    'back_AgencyInfoIndex', __name__)
back_AgencyInfoIndex.secret_key = 'abc'
conn = importPackage.conn
pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_AgencyInfoIndex.route('/backAgencyInfoIndex', methods=['GET', 'POST'])
def backExamRegister():
    cur = conn.cursor()
    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_02_Agency_Register/back_AgencyInfo_Index.html')
