from publicUseFunction import importPackage, dbConnection
back_UnitImage = importPackage.Blueprint('back_UnitImage', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_UnitImage.route('/backUnitImage')
def backPaymentSetting():

    conn = pool.getconn()

    user_id = importPackage.session['user_id']
    user_name = importPackage.session['user_name']

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM "back_07_UnitImageSetting" """)
            result = cursor.fetchall()
    except Exception as e:
        result = None
        print('Error')
    finally:
        cursor.close()
        pool.putconn(conn)
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_07_UnitImageSetting/back_UnitImage.html', result=result, user_name=user_name)
