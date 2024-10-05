from publicUseFunction import importPackage, dbConnection
back_NormalQuestionDesSetting = importPackage.Blueprint(
    'back_NormalQuestionDesSetting', __name__)
conn = importPackage.conn


@back_NormalQuestionDesSetting.route('/backNormalQuestionDesSetting', methods=['GET', 'POST'])
def backNormalQuestionDesSetting():

    cursor = conn.cursor()

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    cursor.execute(
        """ select "normalQuestionTitle" from "back_NormalQuestion" """)
    resultSearch = cursor.fetchall()

    cursor.execute(
        """ SELECT * from "back_NormalDesQuestion" """)

    result = cursor.fetchall()

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_04_NormalQuestionSetting/back_NormalQuestionDesSetting.html', resultSearch=resultSearch, result=result, user_name=user_name)
