from publicUseFunction import importPackage, dbConnection
back_NormalQuestionDesAppend = importPackage.Blueprint(
    'back_NormalQuestionDesAppend', __name__)
conn = importPackage.conn

pool = importPackage.psycopg2.pool.ThreadedConnectionPool(
    minconn=1, maxconn=10, dsn=importPackage.DB_URI)


@back_NormalQuestionDesAppend.route('/backNormalQuestionDesAppend', methods=['GET', 'POST'])
def backNormalQuestionDesAppend():

    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    conn = pool.getconn()
    cursor = conn.cursor()

    if importPackage.request.method == "POST":
        selectMenu = importPackage.request.form['selectMenu']
        normalQuestionDesTitle = importPackage.request.form['normalQuestionDesTitle']
        normalQuestionDesContext = importPackage.request.form['normalQuestionDesContext']
        cursor.execute(""" insert into "back_NormalDesQuestion"("normalQuestionCode","normalQuestionDesTitle","normalQuestionDesContext")
                           values(%s,%s,%s) """, (selectMenu, normalQuestionDesTitle, normalQuestionDesContext))
        conn.commit()

    cursor.execute(
        """ select "normalQuestionTitle","normalQuestionSort" from "back_NormalQuestion" """)
    result = cursor.fetchall()
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_04_NormalQuestionSetting/back_NormalQuestionDesAppend.html', result=result, user_name=user_name, DateTime=formatted_time)
