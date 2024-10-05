from publicUseFunction import importPackage, dbConnection
back_NewsAppend = importPackage.Blueprint('back_NewsAppend', __name__)
conn = importPackage.conn

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_NewsAppend.route('/backNewsAppend', methods=['GET', 'POST'])
def backNewsAppend():

    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    user = importPackage.session['user_id']
    user_name = importPackage.session.get('user_name')

    conn = pool.getconn()
    cursor = conn.cursor()

    Title = str(importPackage.request.args.get('Title'))

    if importPackage.request.method == "POST":
        inputSubTitle = importPackage.request.form['inputSubTitle']
        inputDes = importPackage.request.form['inputDes']
        inputContext = importPackage.request.form['inputContext']
        inputTitle = importPackage.request.form['inputTitle']
        upLoadTime = importPackage.request.form['upLoadTime']
        RemoveTime = importPackage.request.form['RemoveTime']
        cursor = conn.cursor()
        cursor.execute(
            """ INSERT INTO "back_NewsSetting" ("inputSubTitle","inputDes","inputContext","inputTitle","UploadTime","RemoveTime")
                VALUES (%s,%s,%s,%s,%s,%s) """, (inputSubTitle, inputDes, inputContext, inputTitle, upLoadTime, RemoveTime))
        conn.commit()
        conn.close()
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_03_NewSetting/back_NewsAppend.html', user_name=user_name, DateTime=formatted_time)
