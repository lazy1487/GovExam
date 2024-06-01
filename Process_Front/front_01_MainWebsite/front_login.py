from publicUseFunction import importPackage, dbConnection
from publicUseFunction.FunctionSelect.Functionselect import get_user
front_Login = importPackage.Blueprint('front_Login', __name__)
front_Login.secret_key = 'abc'


@front_Login.route('/login', methods=['GET', 'POST'])
def login():
    if importPackage.request.method == 'POST':
        username = importPackage.request.form['username']
        password = importPackage.request.form['password']
        user = get_user(username, password)
        if user:
            importPackage.session['user_id'] = user[0]
            return importPackage.redirect(importPackage.url_for('front_Index.frontIndex'))
        else:
            return "登入失败，請检查用帳號跟密碼。"
    return importPackage.render_template('前台網頁/front_01_MainWebsite/Front_login.html')
