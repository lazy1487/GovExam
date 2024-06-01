from publicUseFunction import importPackage, dbConnection
back_NoticeSetting = importPackage.Blueprint('back_NoticeSetting', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

@back_NoticeSetting.route('/backNoticeSetting',methods=['get'])
def backAgencyRecommendSetting():
    conn = pool.getconn()
    cursor = conn.cursor()
    try:
        with conn.cursor() as cursor:
            cursor.execute(""" select "inputTitle" from "back_NoticeSetting" """)
            result = cursor.fetchall()
    except Exception as e:
        result=None
    finally:
        cursor.close()
        pool.putconn(conn)
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_05_NoticesSetting/back_NoticeSetting.html',result=result)
