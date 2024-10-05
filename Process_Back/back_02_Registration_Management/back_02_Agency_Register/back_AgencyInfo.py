from publicUseFunction import importPackage, dbConnection
back_AgencyInfo = importPackage.Blueprint(
    'back_AgencyInfo', __name__)
back_AgencyInfo.secret_key = 'abc'
conn = importPackage.conn
pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)

@back_AgencyInfo.route('/backAgencyInfo', methods=['GET', 'POST'])
def backExamRegister():

    user_id = importPackage.session.get("user_id")
    user_name = importPackage.session.get("user_name")

    cur = conn.cursor()
    with conn.cursor() as cur:
        cur.execute("""SELECT "AgencyDepartmentID","AgencyDepartmentName","AgencyDepartmentPhone" FROM "back_AgencyInfo" """)
        result = cur.fetchall()
    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_02_Agency_Register/back_AgencyInfo.html',result=result,user_name=user_name)