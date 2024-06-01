from publicUseFunction import importPackage, dbConnection
back_CarouselModify = importPackage.Blueprint('back_CarouselModify', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_CarouselModify.route('/backCarouselModify', methods=['GET', 'POST'])
def backCarouselModify():
    user = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()

    Title = str(importPackage.request.args.get('Title'))

    if importPackage.request.method == "POST":
        Title = importPackage.request.form['Title']

        inputTitle = importPackage.request.form['inputTitle']
        imageDes = importPackage.request.form['imageDes']
        selected = importPackage.request.form['selected']
        inputURL = importPackage.request.form['inputURL']
        imageFile = importPackage.request.form['imageFile']
        phoneimageFile = importPackage.request.form['phoneimageFile']
        upLoadTime = importPackage.request.form['upLoadTime']
        RemoveTime = importPackage.request.form['RemoveTime']

        try:
            with conn.cursor() as cursor:
                cursor = conn.cursor()
                cursor.execute(
                    """UPDATE "back_Carousel" SET "title"=%s, "imgDescript"=%s ,"linkOpen"=%s,
                                                "linkUrl"=%s,"Carousel_compute"=%s,
                                                "Carousel_cellphone"=%s,"UploadTime"=%s,"RemovedTime"=%s
                    WHERE "title"=%s""", (inputTitle, imageDes, selected, inputURL,
                                          imageFile, phoneimageFile, upLoadTime, RemoveTime, Title))
                conn.commit()
        except Exception as e:
            result = None
            print('Errora')
        else:
            cursor.execute(
                """SELECT * FROM "back_Carousel" WHERE "title" = %s """, (inputTitle,))
            result = cursor.fetchall()
            return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselModify.html', result=result, Handler=user, DateTime=formatted_time, Title=inputTitle)
        finally:
            cursor.close()
            pool.putconn(conn)

        return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselModify.html', result=result, Handler=user, DateTime=formatted_time)

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """ SELECT * FROM  "back_Carousel" where "title"=%s """, (Title,))
            result = cursor.fetchall()

    except Exception as e:
        result = None
        print('Errorb')
    finally:
        cursor.close()
        pool.putconn(conn)

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselModify.html', result=result, handler=user, DateTime=formatted_time, Title=Title)
