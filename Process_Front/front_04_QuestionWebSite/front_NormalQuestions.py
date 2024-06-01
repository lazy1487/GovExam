from publicUseFunction import importPackage, dbConnection
front_NormalQuestions = importPackage.Blueprint(
    'main_NormalQuestions', __name__)
front_NormalQuestions.secret_key = 'abc'


@front_NormalQuestions.route('/')
@front_NormalQuestions.route('/frontNormalQuestions')
def index():
    return importPackage.render_template('前台網頁/front_04_QuestionWebSite/front_NormalQuestions.html')
