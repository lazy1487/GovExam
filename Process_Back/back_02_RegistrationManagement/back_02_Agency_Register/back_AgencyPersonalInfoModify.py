from publicUseFunction import importPackage, dbConnection
back_AgencyPersonalInfoModify = importPackage.Blueprint(
    'back_AgencyPersonalInfoModify', __name__)
back_AgencyPersonalInfoModify.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

conn = importPackage.conn

@back_AgencyPersonalInfoModify.route('/backAgencyPersonalInfoModify', methods=['GET', 'POST'])
def backAgencyPersonalInfoModify():

    # with conn.cursor() as cur:
    #     cur.execute("""SELECT "AgencyPersonName","AgencyPersonEmail","AgencyPersonPhone",
    #                           "AgencyPersonID","Agency" FROM "back_AgencyPersonalInfo" """)
    #     result = cur.fetchall()
    return importPackage.render_template('後台網頁/back_02_Registration _Management/back_02_Agency_Register/back_AgencyPersonalInfoModify.html')
