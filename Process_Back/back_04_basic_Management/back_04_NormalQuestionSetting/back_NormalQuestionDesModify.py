from publicUseFunction import importPackage, dbConnection
back_NormalQuestionDesModify = importPackage.Blueprint('back_NormalQuestionDesModify', __name__)
conn = importPackage.conn

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=10, dsn=importPackage.DB_URI)

@back_NormalQuestionDesModify.route('/backNormalQuestionDesModify',methods=['GET','POST'])
def backNormalQuestionDesModify():

    user = importPackage.session['user_id']
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    conn = pool.getconn()
    cursor = conn.cursor()

    Style = str(importPackage.request.args.get('Style'))
    Title = str(importPackage.request.args.get('Title'))

    if importPackage.request.method == "POST":

        Style = importPackage.request.form['Style']
        Title = importPackage.request.form['Title']
        selectMenu = importPackage.request.form['selectMenu']
        normalQuestionDesTitle = importPackage.request.form['normalQuestionDesTitle']
        normalQuestionDesContext = importPackage.request.form['normalQuestionDesContext']
        try:
            with conn.cursor() as cursor:
                cursor = conn.cursor()
                cursor.execute("""UPDATE "back_NormalDesQuestion" SET "normalQuestionDesTitle"=%s, "normalQuestionDesContext"=%s 
                                  WHERE "normalQuestionDesTitle"=%s""", (normalQuestionDesTitle,normalQuestionDesContext, Title))
                conn.commit()

        except Exception as e:
            result = None
            print('Error')
        else:
            cursor.execute("""SELECT * FROM "back_NormalDesQuestion" WHERE "normalQuestionDesTitle" = %s """,(normalQuestionDesTitle,))
            result = cursor.fetchall()
        finally:
            cursor.close()
            pool.putconn(conn)
        
        return importPackage.render_template('後台網頁/back_04_basic_Management/back_04_NormalQuestionSetting/back_NormalQuestionDesModify.html',result=result,Handler=user,DateTime=formatted_time)
    else:
        try:
            with conn.cursor() as cursor:
                cursor.execute("""SELECT * FROM "back_NormalDesQuestion" WHERE "normalQuestionDesTitle" = %s """,(Title,))
                result = cursor.fetchall()

        except Exception as e:
            result = None
            print('ErrorB')
        finally:
            cursor.close()
            pool.putconn(conn)

        return importPackage.render_template('後台網頁/back_04_basic_Management/back_04_NormalQuestionSetting/back_NormalQuestionDesModify.html',result=result,Title=Title,Style=Style,Handler=user,DateTime=formatted_time)
