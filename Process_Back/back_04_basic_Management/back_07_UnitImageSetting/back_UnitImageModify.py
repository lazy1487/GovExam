from publicUseFunction import importPackage, dbConnection
back_UnitImageModify = importPackage.Blueprint(
    'back_UnitImageModify', __name__)
back_UnitImageModify.secret_key = 'abc'

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_UnitImageModify.route('/backUnitImageModify', methods=['GET', 'POST'])
def backUnitImageModify():

    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()

    user_id = importPackage.session['user_id']
    user_name = importPackage.session['user_name']

    Title = str(importPackage.request.args.get('Title'))

    if importPackage.request.method == "POST":
        Title = importPackage.request.form['Title']
        hiddentitle = importPackage.request.form['hiddentitle']
        hiddeninputfile = importPackage.request.form['hiddeninputfile']
        hiddenimageDes = importPackage.request.form['hiddenimageDes']

        try:
            base_directory = importPackage.os.path.dirname(
                importPackage.os.path.abspath(__file__)).split("\\")
            print("static\\"+"後台網頁\\" +
                  base_directory[-2]+"\\"+base_directory[-1]+'\\'+'images\\'+hiddeninputfile)
            with conn.cursor() as cursor:
                cursor = conn.cursor()
                cursor.execute("""UPDATE "back_UnitImage" SET "webTitle"=%s, "imageUrl"=%s, "imageDes"=%s WHERE "webTitle"=%s""",
                               (hiddentitle, "static\\"+"後台網頁\\"+base_directory[-2]+"\\"+base_directory[-1]+'\\'+'images\\'+hiddeninputfile, hiddenimageDes, Title))
                conn.commit()

        except Exception as e:
            result = None
            print('Error')
        else:
            cursor.execute(
                """SELECT * FROM "back_UnitImage" WHERE "webTitle" = %s """, (hiddentitle,))
            result = cursor.fetchall()
        finally:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """SELECT * FROM "back_UnitImage" order by "webSort" """)
                    result = cursor.fetchall()
            except Exception as e:
                result = None
                print('Error')
            finally:
                cursor.close()
                pool.putconn(conn)
            return importPackage.render_template('後台網頁/back_04_basic_Management/back_07_UnitImageSetting/back_UnitImage.html', result=result)
    else:
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """SELECT * FROM "back_07_UnitImageSetting" WHERE "web_Title" = %s order by "web_Sort" """, (Title,))
                result = cursor.fetchall()
        except Exception as e:
            result = None
            print('ErrorB')
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_04_basic_Management/back_07_UnitImageSetting/back_UnitImageModify.html', result=result, user_name=user_name, DateTime=formatted_time, Title=Title)
