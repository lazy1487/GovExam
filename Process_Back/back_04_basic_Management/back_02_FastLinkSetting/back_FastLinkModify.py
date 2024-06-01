from publicUseFunction import importPackage, dbConnection
back_FastLinkModify = importPackage.Blueprint('back_FastLinkModify', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)

# @back_FastLinkModify.route('/backFastLinkModify', methods=['GET', 'POST'])


@back_FastLinkModify.route('/backFastLinkModify', methods=['GET', 'POST'])
def backFastLinkModify():

    user = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    Title = str(importPackage.request.args.get('Title'))

    conn = pool.getconn()

    if importPackage.request.method == "POST":
        Title = importPackage.request.form['Title']
        inputTitle = importPackage.request.form['inputTitle']
        imageDes = importPackage.request.form['imageDes']
        selected = importPackage.request.form['selected']
        inputURL = importPackage.request.form['inputURL']
        imageFile = importPackage.request.form['imageFile']
        print(Title,inputTitle,imageDes,selected,inputURL,imageFile)
        try:
            with conn.cursor() as cursor:
                cursor = conn.cursor()
                cursor.execute(
                    """UPDATE "back_FastLinkSetting" SET "inputTitle"=%s, "imageDes"=%s,"openStyle"=%s,"linkUrl"=%s,"imageUrl"=%s 
                        WHERE "inputTitle"=%s""", (inputTitle, imageDes, selected, inputURL, imageFile, Title))
                conn.commit()

        except Exception as e:
            result = None
            print('Errora')
        else:
            cursor.execute(
                """SELECT * FROM "back_FastLinkSetting" """)
            result = cursor.fetchall()
        finally:
            cursor.close()
            pool.putconn(conn)

        return importPackage.render_template('後台網頁/back_04_basic_Management/back_02_FastLinkSetting/back_FastLinkSetting.html', result=result)
    else:
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """ SELECT * FROM  "back_FastLinkSetting"  WHERE "inputTitle" = %s """, (Title,))
                result = cursor.fetchall()
        except Exception as e:
            result = None
            print('Errorb')
        finally:
            cursor.close()
            pool.putconn(conn)

        return importPackage.render_template('後台網頁/back_04_basic_Management/back_02_FastLinkSetting/back_FastLinkModify.html', 
                                              result=result, handler=user, DateTime=formatted_time, Title=Title)
