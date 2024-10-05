from publicUseFunction import importPackage, dbConnection
back_NormalQuestionSub = importPackage.Blueprint(
    'back_NormalQuestionSub', __name__)
conn = importPackage.conn


@back_NormalQuestionSub.route('/backNormalQuestionSub', methods=['GET', 'POST'])
def backNormalQuestionSub():

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_04_NormalQuestionSetting/back_NormalQuestionSub.html', user_name=user_name)
