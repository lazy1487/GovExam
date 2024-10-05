from publicUseFunction import importPackage, dbConnection
back_NoticeSub = importPackage.Blueprint('back_NoticeSub', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

@back_NoticeSub.route('/backNoticeSub',methods=['GET','POST'])
def backNoticeSub():

    user = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_05_NoticesSetting/back_NoticeSub.html',handler=user,DateTime=formatted_time)
