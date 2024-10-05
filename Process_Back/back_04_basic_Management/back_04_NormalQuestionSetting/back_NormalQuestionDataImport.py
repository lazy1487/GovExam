from publicUseFunction import importPackage, dbConnection
back_NormalQuestionDataImport = importPackage.Blueprint(
    'back_NormalQuestionDataImport', __name__)


@back_NormalQuestionDataImport.route('/backNormalQuestionDataImport')
def backNormalQuestionDataImport():

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    return importPackage.render_template('後台網頁/back_04_basic_Management/back_04_NormalQuestionSetting/back_NormalQuestionDataImport.html')
