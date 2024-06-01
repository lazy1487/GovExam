from publicUseFunction import importPackage, dbConnection
back_CarouselSort = importPackage.Blueprint('back_CarouselSort', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

@back_CarouselSort.route('/backCarouselSort', methods=['GET', 'POST'])
def backCarouselAppend():

    user = importPackage.session['user_id']
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()

    # if importPackage.request.method == "POST":
    #     cursor = conn.cursor()
    #     cursor.execute(
    #         """SELECT "title" FROM "back_Carousel" """)
    #     result = cursor.fetchall()
    #     conn.close()
    #     return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselSort.html', result=result, Handler=user, DateTime=formatted_time)

    try:
        with conn.cursor() as cursor:
            cursor.execute("""SELECT "title" FROM "back_Carousel" """)
            result = cursor.fetchall()
    except Exception as e:
        result=None
        print('Error')
    finally:
        cursor.close()
        pool.putconn(conn)
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselSort.html', result=result, Handler=user, DateTime=formatted_time)
