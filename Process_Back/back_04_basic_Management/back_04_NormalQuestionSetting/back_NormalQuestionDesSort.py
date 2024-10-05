from publicUseFunction import importPackage, dbConnection
back_NormalQuestionDesSort = importPackage.Blueprint(
    'back_NormalQuestionDesSort', __name__)
conn = importPackage.conn


@back_NormalQuestionDesSort.route('/backNormalQuestionDesSort')
def backNormalQuestionDesSort():
    cursor = conn.cursor()

    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    cursor.execute(
        """ select "normalQuestionTitle","normalQuestionSort" from "back_NormalQuestion" """)
    result = cursor.fetchall()
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_04_NormalQuestionSetting/back_NormalQuestionDesSort.html', result=result, user_name=user_name, DateTime=formatted_time)
