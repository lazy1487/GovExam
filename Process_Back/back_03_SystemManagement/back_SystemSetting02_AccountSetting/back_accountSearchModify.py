from publicUseFunction import importPackage, dbConnection
back_AccountSearchModify = importPackage.Blueprint(
    'back_AccountSearchModify', __name__)
back_AccountSearchModify.secret_key = 'abc'


@back_AccountSearchModify.route('/backaccountSearchModify')
def backAccountSearchModify():
    return importPackage.render_template('後台網頁/back_03_System_Management/back_02_AccountSetting/Back_accountSearchModify.html')
