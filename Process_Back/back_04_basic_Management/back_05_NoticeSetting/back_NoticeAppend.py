from publicUseFunction import importPackage, dbConnection
back_NoticeAppend = importPackage.Blueprint('back_NoticeAppend', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

@back_NoticeAppend.route('/backNoticeAppend',methods=['GET','POST'])
def backNoticeAppend():

    PublicUseBackName = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()

    try:
        if importPackage.request.method=='POST':
            inputTitle = importPackage.request.form['inputTitle']
            imageDes = importPackage.request.form['imageDes']

            if (inputTitle!='' and imageDes!=''):
                cursor.execute(""" insert into "back_NoticeSetting"("inputTitle","imageDes")
                                values(%s,%s) """,(inputTitle,imageDes))
                conn.commit()
    except Exception as e:
        result=None
        print('Error')
    finally:
        cursor.close()
        pool.putconn(conn)
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_05_NoticesSetting/back_NoticeAppend.html',handler=PublicUseBackName,DateTime=formatted_time)
