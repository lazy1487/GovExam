from publicUseFunction import importPackage, dbConnection
back_CarouselImageShow = importPackage.Blueprint(
    'back_CarouselImageShow', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)



@back_CarouselImageShow.route('/backCarouselImageShow', methods=['GET', 'POST'])
def backCarouselImageShow():

    Title = str(importPackage.request.args.get('Title'))

    conn = pool.getconn()
    cursor = conn.cursor()

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """ SELECT "Carousel_compute","Carousel_cellphone" FROM "back_Carousel" where "title"=%s """, (Title,))
            result = cursor.fetchall()

    except Exception as e:
        result = None
        print('Errorb')
    finally:
        cursor.close()
        pool.putconn(conn)

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselImageShow.html',result=result,Title=Title)
