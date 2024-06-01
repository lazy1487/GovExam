from publicUseFunction import importPackage, dbConnection
back_ExamInfoSetting = importPackage.Blueprint(
    'back_ExamInfoSetting', __name__)
back_ExamInfoSetting.secret_key = 'abc'


@back_ExamInfoSetting.route('/backExamInfoSetting', methods=['GET', 'POST'])
def backExamRegister():
    return importPackage.render_template('後台網頁/back_02_Registration _Management/back_01_ExamStudent_Register/back_ExamInfoSetting.html')
