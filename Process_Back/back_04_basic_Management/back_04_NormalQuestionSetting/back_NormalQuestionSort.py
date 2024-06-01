from publicUseFunction import importPackage, dbConnection
back_NormalQuestionSort = importPackage.Blueprint(
    'back_NormalQuestionSort', __name__)
conn = importPackage.conn


@back_NormalQuestionSort.route('/backNormalQuestionSort')
def backNormalQuestionSort():
    PublicUseBackName = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")
    cursor = conn.cursor()
    cursor.execute(
        """ select "normalQuestionTitle" from "back_NormalQuestion" """)
    result = cursor.fetchall()
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_04_NormalQuestionSetting/back_NormalQuestionSort.html',
                                         result=result, handler=PublicUseBackName, DateTime=formatted_time)
