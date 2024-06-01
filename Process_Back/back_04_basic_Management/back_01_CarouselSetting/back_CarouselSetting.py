from publicUseFunction import importPackage, dbConnection
back_CarouselSetting = importPackage.Blueprint(
    'back_CarouselSetting', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_CarouselSetting.route('/backCarouselSetting', methods=['GET', 'POST'])
def backCarouselSetting():

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

    try:
        with conn.cursor() as cursor:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT "title","Carousel_compute","UploadTime","RemovedTime","uuid32" FROM "back_Carousel" """)
            result = cursor.fetchall()
    except Exception as e:
        result = None
        print('Error')
    finally:
        cursor.close()
        pool.putconn(conn)

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselSetting.html', result=result)

@back_CarouselSetting.route('/backCarouselSettingDelete', methods=['GET', 'POST'])
def backCarouselSettingDelete():
    conn = pool.getconn()
    if importPackage.request.method == 'POST':
        Title = importPackage.request.form.get('Title')
        
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """DELETE FROM "back_Carousel" WHERE "title" = %s""", (Title,))
                conn.commit()
        except Exception as e:
            result = None
            print('Error')
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.redirect(importPackage.url_for('back_CarouselSetting.backCarouselSetting'))
    else:
        try:
            cursor.execute(
                """SELECT "title","imgDescript","UploadTime","RemovedTime" FROM "back_Carousel" """)
            result = cursor.fetchall()
        except:
            result = None
            print('Error')
        finally:
            cursor.close()
            pool.putconn(conn)
        return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselSetting.html', result=result)