from publicUseFunction import importPackage, dbConnection
back_FastLinkImageShow = importPackage.Blueprint(
    'back_FastLinkImageShow', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)



@back_FastLinkImageShow.route('/backFastLinkImageShow', methods=['GET', 'POST'])
def backFastLinkImageShow():

    Title = str(importPackage.request.args.get('Title'))

    conn = pool.getconn()
    cursor = conn.cursor()

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """ SELECT "imageUrl" FROM "back_FastLinkSetting" where "inputTitle"=%s """, (Title,))
            result = cursor.fetchall()

    except Exception as e:
        result = None
        print('Errorb')
    finally:
        cursor.close()
        pool.putconn(conn)

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_02_FastLinkSetting/back_FastLinkImageShow.html',result=result)