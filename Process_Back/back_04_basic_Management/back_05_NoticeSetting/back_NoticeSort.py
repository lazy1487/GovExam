from publicUseFunction import importPackage, dbConnection
back_NoticeSort = importPackage.Blueprint('back_NoticeSort', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

conn = importPackage.conn
@back_NoticeSort.route('/backNoticeSort')
def backNoticeSort():

    PublicUseBackName = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()
    
    try:
        cursor.execute(""" select "inputTitle","inputTitleSort" from "back_NoticeSetting" """)
        result = cursor.fetchall()
    except Exception as e:
        result=None
        print('Error')
    finally:
        cursor.close()
        pool.putconn(conn)
    
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_05_NoticesSetting/back_NoticeSort.html',result=result,handler=PublicUseBackName,DateTime=formatted_time)
