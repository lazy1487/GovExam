from publicUseFunction import importPackage, dbConnection
back_ExamRegister = importPackage.Blueprint('back_ExamRegister', __name__)
back_ExamRegister.secret_key = 'abc'


@back_ExamRegister.route('/backExamRegister', methods=['GET', 'POST'])
def backExamRegister():

    user_id = importPackage.session.get('user_id')
    user_name = importPackage.session.get('user_name')

    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamRegister.html', user_name=user_name)
