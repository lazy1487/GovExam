from publicUseFunction import importPackage, dbConnection
back_CarouselSort = importPackage.Blueprint('back_CarouselSort', __name__)

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_CarouselSort.route('/backCarouselSort', methods=['GET'])
def backCarouselAppend():
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    user = importPackage.session['user_id']
    user_name = importPackage.session.get('user_name')

    conn = pool.getconn()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT "title","CarouselSort" FROM "back_Carousel" """)
            result = cursor.fetchall()
    except Exception as e:
        result = None
        print('Error:', e)
    finally:
        cursor.close()
        pool.putconn(conn)
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_01_CarouselSetting/back_CarouselSort.html', result=result, Handler=user, DateTime=formatted_time, user_name=user_name)


@back_CarouselSort.route('/update_sort', methods=['POST'])
def update_sort():
    data = importPackage.request.json
    try:
        conn = pool.getconn()
        with conn.cursor() as cursor:
            for item in data:
                cursor.execute("""UPDATE "back_Carousel" SET "CarouselSort" = %s WHERE "title" = %s""",
                               (item['sort'], item['title']))
            conn.commit()
        return importPackage.jsonify({'status': 'success'})
    except Exception as e:
        print('Error:', e)
        return importPackage.jsonify({'status': 'failure'})
    finally:
        cursor.close()
        pool.putconn(conn)
