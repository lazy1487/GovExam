from publicUseFunction import importPackage, dbConnection
back_NormalQuestionDesSub = importPackage.Blueprint(
    'back_NormalQuestionDesSub', __name__)
conn = importPackage.conn


@back_NormalQuestionDesSub.route('/backNormalQuestionDesSub', methods=['GET', 'POST'])
def backNormalQuestionDesSub():

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_04_NormalQuestionSetting/back_NormalQuestionDesSub.html', user_name=user_name)
