from publicUseFunction import importPackage, dbConnection
back_AgencyInfoSub = importPackage.Blueprint(
    'back_AgencyInfoSub', __name__)
back_AgencyInfoSub.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

conn = importPackage.conn


@back_AgencyInfoSub.route('/backAgencyInfoSub', methods=['GET', 'POST'])
def backAgencyInfoSub():
    
    AgencyID = str(importPackage.request.args.get('AgencyID'))

    with conn.cursor() as cursor:
        cursor.execute("""SELECT * FROM "back_AgencyInfo" Where "AgencyID"=%s """,(AgencyID,))
        result = cursor.fetchall()
    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_02_Agency_Register/back_AgencyInfoSub.html',result=result)
