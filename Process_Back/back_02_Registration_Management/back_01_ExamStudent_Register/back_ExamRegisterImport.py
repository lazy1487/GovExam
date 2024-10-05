from publicUseFunction import importPackage, dbConnection
back_ExamRegisterImport = importPackage.Blueprint(
    'back_ExamRegisterImport', __name__)
back_ExamRegisterImport.secret_key = 'abc'


@back_ExamRegisterImport.route('/backExamRegisterImport', methods=['GET', 'POST'])
def backExamRegisterAppend():
    user_id = importPackage.session.get("user_id")
    user_name = importPackage.session.get("user_name")
    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamRegisterImport.html',user_name=user_name)
