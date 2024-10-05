from publicUseFunction import importPackage, dbConnection
back_NewsModify = importPackage.Blueprint('back_NewsModify', __name__)
conn = importPackage.conn

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_NewsModify.route('/backNewsModify', methods=['GET', 'POST'])
def backNewsModify():

    conn = pool.getconn()
    cursor = conn.cursor()

    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    Title = str(importPackage.request.args.get('Title'))

    if importPackage.request.method == "POST":
        Title = importPackage.request.form['Title']
        inputSubTitle = importPackage.request.form['inputSubTitle']
        inputDes = importPackage.request.form['inputDes']
        inputContext = importPackage.request.form['inputContext']
        inputTitle = importPackage.request.form['inputTitle']
        UploadTime = importPackage.request.form['UploadTime']
        RemoveTime = importPackage.request.form['RemoveTime']

        try:
            with conn.cursor() as cursor:
                cursor = conn.cursor()
                cursor.execute("""UPDATE "back_NewsSetting" SET "inputSubTitle"=%s, "inputDes"=%s,"inputContext"=%s,"inputTitle"=%s,"UploadTime"=%s,"RemoveTime"=%s
                                    WHERE "inputSubTitle"=%s""", (inputSubTitle, inputDes, inputContext, inputTitle, UploadTime, RemoveTime, Title))
                conn.commit()

        except Exception as e:
            result = None
            print('Error')
        else:
            cursor.execute(
                """SELECT * FROM "back_NewsSetting" WHERE "inputSubTitle" = %s """, (inputSubTitle,))
            result = cursor.fetchall()
        finally:
            cursor.close()
            pool.putconn(conn)

        return importPackage.render_template('後台網頁/back_04_basic_Management/back_03_NewSetting/back_NewsModify.html', result=result, DateTime=formatted_time, user_name=user_name)
    else:
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT * FROM "back_NewsSetting" WHERE "inputSubTitle" = %s""", (Title,))
                result = cursor.fetchall()
        except Exception as e:
            result = None
            print('Error')
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_04_basic_Management/back_03_NewSetting/back_NewsModify.html', result=result, DateTime=formatted_time, Title=Title, user_name=user_name)


@back_NewsModify.route('/backNewsModifyDelete', methods=['GET', 'POST'])
def backNewsModifyDelete():
    Title = str(importPackage.request.args.get('Title'))

    conn = pool.getconn()
    if importPackage.request.method == 'POST':
        Title = importPackage.request.form['Title']
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """DELETE FROM "back_NewsSetting" WHERE "inputSubTitle" = %s""", (Title,))
                conn.commit()
        except Exception as e:
            result = None
            print('ErrorB')
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.redirect(importPackage.url_for('back_NewsModify.backNewsModifyDelete'))
    else:
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT "inputSubTitle", "UploadTime", "RemoveTime" FROM "back_NewsSetting" """)
                result = cursor.fetchall()
        except:
            result = None
            print('ErrorA')
        finally:
            cursor.close()
            pool.putconn(conn)

        return importPackage.render_template('後台網頁/back_04_basic_Management/back_03_NewSetting/back_NewsSetting.html', result=result, Title=Title, user_name=user_name)
