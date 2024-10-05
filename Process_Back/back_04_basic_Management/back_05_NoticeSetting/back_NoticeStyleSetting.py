from publicUseFunction import importPackage, dbConnection
back_NoticeStyleSetting = importPackage.Blueprint(
    'back_NoticeStyleSetting', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_NoticeStyleSetting.route('/backNoticeStyleSetting', methods=['get'])
def backNoticeStyleSetting():
    conn = pool.getconn()
    cursor = conn.cursor()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """ select "noticeStyleCode","noticeStyleTitle","noticeStyleIsUse" from "back_NoticeStyleSetting" """)
            result = cursor.fetchall()
    except Exception as e:
        result = None
    finally:
        cursor.close()
        pool.putconn(conn)

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_05_NoticesSetting/back_NoticeStyleSetting.html', result=result)
