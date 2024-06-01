from publicUseFunction import importPackage, dbConnection
back_UnitImageShow = importPackage.Blueprint(
    'back_UnitImageShow', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)



@back_UnitImageShow.route('/backUnitImageShow', methods=['GET', 'POST'])
def backUnitImageShow():

    Title = str(importPackage.request.args.get('Title'))

    conn = pool.getconn()
    cursor = conn.cursor()

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """ SELECT "imageUrl" FROM "back_UnitImage" where "webTitle"=%s """, (Title,))
            result = cursor.fetchall()

    except Exception as e:
        result = None
        print('Errorb')
    finally:
        cursor.close()
        pool.putconn(conn)

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_07_UnitImageSetting/back_UnitImageShow.html',result=result)