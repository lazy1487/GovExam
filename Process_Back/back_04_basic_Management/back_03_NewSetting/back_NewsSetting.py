from publicUseFunction import importPackage, dbConnection
back_NewsSetting = importPackage.Blueprint('back_NewsSetting', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=999999999999, dsn=importPackage.DB_URI)


@back_NewsSetting.route('/backNewsSetting', methods=['GET', 'POST'])
def backNewsSetting():

    conn = pool.getconn()

    user = importPackage.session['user_id']
    user_name = importPackage.session.get('user_name')

    page = importPackage.request.args.get('page', 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page

    if importPackage.request.method == 'POST':
        cursor = conn.cursor()
        inputSubTitle = importPackage.request.form['inputSubTitle']
        UploadTime = importPackage.request.form['UploadTime']
        RemoveTime = importPackage.request.form['RemoveTime']

        try:
            try:
                UploadTime = importPackage.datetime.datetime.strptime(
                    UploadTime, '%Y-%m-%d')  # 假設日期格式為 YYYY-MM-DD
                RemoveTime = importPackage.datetime.datetime.strptime(
                    RemoveTime, '%Y-%m-%d')  # 假設日期格式為 YYYY-MM-DD
            except ValueError:
                # 處理無效日期字串的情況，例如設置為 None 或者其他特定的預設值
                UploadTime = None
                RemoveTime = None

            if (inputSubTitle == '' or UploadTime == '' or RemoveTime == ''):
                cursor.execute(""" Select "inputSubTitle","UploadTime","RemoveTime"
                            from "back_NewsSetting" """)
                result = cursor.fetchall()
            else:
                cursor.execute(""" Select "inputSubTitle","UploadTime","RemoveTime" from "back_NewsSetting"
                                Where  ("inputSubTitle"=%s) or ("UploadTime"=%s and "RemoveTime"=%s) """,
                               (inputSubTitle, UploadTime, RemoveTime))
                result = cursor.fetchall()
        except Exception as e:
            result = None
            print('Error')
        finally:
            cursor.close()
            pool.putconn(conn)

        return importPackage.render_template('後台網頁/back_04_basic_Management/back_03_NewSetting/back_NewsSetting.html', result=result)
    else:
        cursor = conn.cursor()
        cursor.execute("""SELECT "inputSubTitle", "UploadTime", "RemoveTime" 
                          FROM "back_NewsSetting" 
                          ORDER BY "UploadTime" ASC 
                          LIMIT %s OFFSET %s""", (per_page, offset))
        result = cursor.fetchall()

        cursor.execute("""SELECT COUNT(*) FROM "back_NewsSetting" """)
        total_rows = cursor.fetchone()[0]
        total_pages = (total_rows + per_page - 1) // per_page  # 計算總頁數

        return importPackage.render_template('後台網頁/back_04_basic_Management/back_03_NewSetting/back_NewsSetting.html', result=result, page=page, total_pages=total_pages, user_name=user_name)
