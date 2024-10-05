from publicUseFunction import importPackage, dbConnection
back_fastLinkSetting = importPackage.Blueprint(
    'back_fastLinkSetting', __name__)
back_fastLinkSetting.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_fastLinkSetting.route('/backfastLinkSetting', methods=['GET', 'POST'])
def backfastLinkSetting():

    user = importPackage.session['user_id']
    user_name = importPackage.session.get('user_name')

    conn = pool.getconn()
    query = """ SELECT "inputTitle", "imageDes", "linkOpen", "linkUrl","image","linkMessageSwitch","linkSwitch","linkMaintainContext","linkCloseStartTime","linkCloseEndTime" FROM "back_FastLinkSetting" """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            # importPackage.session['inputTitle'] = result[1]
    except Exception as e:
        result = None
        print('Error')
    finally:
        cursor.close()
        pool.putconn(conn)

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_02_FastLinkSetting/back_FastLinkSetting.html', result=result, user_name=user_name)
