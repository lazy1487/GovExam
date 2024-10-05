from publicUseFunction import importPackage, dbConnection
back_ExamRegisterModify= importPackage.Blueprint('backExamRegisterModify', __name__)
back_ExamRegisterModify.secret_key = 'abc'

@back_ExamRegisterModify.route('/backExamRegisterModify', methods=['GET', 'POST'])
def backExamRegisterModify():
    return importPackage.render_template('後台網頁/back_02_Registration_Management/back_01_ExamStudent_Register/back_ExamRegisterModify.html')