from publicUseFunction import importPackage, dbConnection
back_ExamRegister= importPackage.Blueprint('back_ExamRegister', __name__)
back_ExamRegister.secret_key = 'abc'

@back_ExamRegister.route('/backExamRegister', methods=['GET', 'POST'])
def backExamRegister():
    return importPackage.render_template('後台網頁/back_02_Registration _Management/back_01_ExamStudent_Register/back_ExamRegister.html')