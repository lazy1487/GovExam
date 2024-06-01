from publicUseFunction import importPackage, dbConnection
front_ForgetPassword = importPackage.Blueprint(
    'main_ForgetPassword', __name__)
front_ForgetPassword.secret_key = 'abc'


@front_ForgetPassword.route('/')
@front_ForgetPassword.route('/frontForgetPassword')
def index():
    return importPackage.render_template('前台網頁/front_01_MainWebSite/front_ForgetPassword.html')
