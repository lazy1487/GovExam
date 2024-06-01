from publicUseFunction import importPackage, dbConnection
from publicUseFunction.FunctionInsert.FunctionInsert import create_user
mainRegister = importPackage.Blueprint('register', __name__)
mainRegister.secret_key = 'abc'


@mainRegister.route('/register', methods=['GET', 'POST'])
def register():
    if importPackage.request.method == 'POST':
        email = importPackage.request.form['email']
        username = importPackage.request.form['username']
        password = importPackage.request.form['password']
        confirm_password = importPackage.request.form['confirm_password']
        if password != confirm_password:
            return "密碼比對錯誤，請重新輸入。"

        # 使用 create_user 函數插入使用者帳號
        create_user(email, username, password)
        return importPackage.redirect(importPackage.url_for('index.index'))
    return importPackage.render_template('前台網頁/Front_register.html')
