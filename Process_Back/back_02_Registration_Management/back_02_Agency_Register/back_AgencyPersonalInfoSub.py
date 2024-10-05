from publicUseFunction import importPackage, dbConnection
back_AgencyPersonalInfoSub = importPackage.Blueprint(
    'back_AgencyPersonalInfoSub', __name__)
back_AgencyPersonalInfoSub.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

@back_AgencyPersonalInfoSub.route('/backAgencyPersonalInfoSub', methods=['GET', 'POST'])
def backAgencyPersonalInfoSub():
    conn = pool.getconn()

    Name = str(importPackage.request.args.get('Name'))

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM "back_AgencyPersonalInfo" Where "AgencyPersonName"=%s """,(Name,))
            result = cursor.fetchall()
    except Exception as e:
        result = None
        print('Error')
    finally:
        cursor.close()
        pool.putconn(conn)
    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_02_Agency_Register/back_AgencyPersonalInfoSub.html',result=result)
