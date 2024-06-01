from publicUseFunction import importPackage, dbConnection
back_NewsAppend = importPackage.Blueprint('back_NewsAppend', __name__)
conn = importPackage.conn


@back_NewsAppend.route('/backNewsAppend', methods=['GET', 'POST'])
def backNewsAppend():
    
    PublicUseBackName = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")
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
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_03_NewSetting/back_NewsAppend.html', Handler=PublicUseBackName, DateTime=formatted_time)
