from publicUseFunction import importPackage, dbConnection
back_UnitImageModify= importPackage.Blueprint('back_UnitImageModify', __name__)
back_UnitImageModify.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

@back_UnitImageModify.route('/backUnitImageModify', methods=['GET', 'POST'])
def backUnitImageModify():

    user = importPackage.session['user_id']
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()

    Title = str(importPackage.request.args.get('Title'))

    if importPackage.request.method == "POST":
        Title = importPackage.request.form['Title']
        inputTitle = importPackage.request.form['inputTitle']
        imageFile = importPackage.request.form['imageFile']
        imageDes = importPackage.request.form['imageDes']
        try:
            with conn.cursor() as cursor:
                cursor = conn.cursor()
                cursor.execute("""UPDATE "back_UnitImage" SET "webTitle"=%s, "imageUrl"=%s, "imageDes"=%s WHERE "webTitle"=%s""", (inputTitle, imageFile,imageDes, Title))
                conn.commit()

        except Exception as e:
            result = None
            print('Error')
        else:
            cursor.execute("""SELECT * FROM "back_UnitImage" WHERE "webTitle" = %s """,(inputTitle,))
            result = cursor.fetchall()
        finally:
            cursor.close()
            pool.putconn(conn)
        
        return importPackage.render_template('後台網頁/back_04_basic_Management/back_07_UnitImageSetting/back_UnitImageModify.html',result=result,Handler=user,DateTime=formatted_time)
        
    else:
        try:
            with conn.cursor() as cursor:
                cursor.execute("""SELECT * FROM "back_UnitImage" WHERE "webTitle" = %s""",(Title,))
                result = cursor.fetchall()
        except Exception as e:
            result = None
            print('ErrorB')
        finally:
            cursor.close()
            pool.putconn(conn)
        
        
        
        return importPackage.render_template('後台網頁/back_04_basic_Management/back_07_UnitImageSetting/back_UnitImageModify.html',result=result,Handler=user,DateTime=formatted_time,Title=Title)