from publicUseFunction import importPackage, dbConnection
front_ExamRegistration = importPackage.Blueprint(
    'main_ExamRegistration', __name__)
front_ExamRegistration.secret_key = 'abc'


@front_ExamRegistration.route('/')
@front_ExamRegistration.route('/frontExamRegistration')
def index():
    return importPackage.render_template('前台網頁/front_02_ExamWebSite/front_ExamRegistration.html')
