from publicUseFunction import importPackage, dbConnection
back_NormalQuestionDesSort = importPackage.Blueprint('back_NormalQuestionDesSort', __name__)
conn = importPackage.conn
@back_NormalQuestionDesSort.route('/backNormalQuestionDesSort')
def backNormalQuestionDesSort():
    cursor = conn.cursor()

    PublicUseBackName = importPackage.session.get('user_name')
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    cursor.execute(""" select "normalQuestionTitle","normalQuestionSort" from "back_NormalQuestion" """)
    result = cursor.fetchall()
    return importPackage.render_template('後台網頁/back_04_basic_Management/back_04_NormalQuestionSetting/back_NormalQuestionDesSort.html',result=result,handler=PublicUseBackName,DateTime=formatted_time)
