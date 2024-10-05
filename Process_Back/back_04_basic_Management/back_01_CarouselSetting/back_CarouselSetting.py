from publicUseFunction import importPackage, dbConnection
back_CarouselSetting = importPackage.Blueprint(
    'back_CarouselSetting', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_CarouselSetting.route('/backCarouselSetting', methods=['GET', 'POST'])
def backCarouselSetting():

    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    user = importPackage.session['user_id']
    user_name = importPackage.session.get('user_name')

    conn = pool.getconn()
    cursor = conn.cursor()

    if importPackage.request.method == "POST":

        inputTitle = importPackage.request.form['inputTitle']
        upLoadTime = importPackage.request.form['upLoadTime']
        RemovedTime = importPackage.request.form['RemovedTime']
        try:
            with conn.cursor() as cursor:
                if (upLoadTime == '' or RemovedTime == ''):
                    cursor.execute(
                        """SELECT "title","Carousel_compute","UploadTime","RemovedTime","uuid32" FROM "back_Carousel" """)
                else:
                    cursor.execute(
                        """SELECT "title", "Carousel_compute", "UploadTime", "RemovedTime","uuid32"
                    FROM "back_Carousel" 
                    WHERE "title" = %s OR ("UploadTime" BETWEEN %s AND %s) OR ("RemovedTime" BETWEEN %s AND %s)""",
                        (inputTitle, upLoadTime, RemovedTime, upLoadTime, RemovedTime))
                    searchresult = cursor.fetchall()
        except Exception as e:
            result = None
            print('Error')
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselSetting.html', searchresult=searchresult)
    else:
        try:
            with conn.cursor() as cursor:
                cursor = conn.cursor()
                cursor.execute(
                    """SELECT * FROM "back_Carousel" """)
                result = cursor.fetchall()
        except Exception as e:
            result = None
            print('Error')
        finally:
            cursor.close()
            pool.putconn(conn)
            print(result)
        return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselSetting.html', result=result, Handler=user, DateTime=formatted_time, user_name=user_name)
