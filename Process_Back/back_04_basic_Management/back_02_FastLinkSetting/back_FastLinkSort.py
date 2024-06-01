from publicUseFunction import importPackage, dbConnection
back_FastLinkSort = importPackage.Blueprint('back_FastLinkSort', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

@back_FastLinkSort.route('/backFastLinkSort', methods=['GET', 'POST'])
def backCarouselAppend():

    PublicUseBackName = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()

    try:
        with  conn.cursor() as cursor:
            cursor.execute(""" SELECT "inputTitle" FROM "back_FastLinkSetting" """)
            result = cursor.fetchall()
    except Exception as e:
        result=None
        print('Error')
    finally:
        cursor.close()
        pool.putconn(conn)
    
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_02_FastLinkSetting/back_FastLinkSort.html',
                                         result=result, Handler=PublicUseBackName, DateTime=formatted_time)
