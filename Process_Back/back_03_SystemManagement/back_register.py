from publicUseFunction import importPackage, dbConnection
backRegister = importPackage.Blueprint('index/backendRegister', __name__)
backRegister.secret_key = 'abc'


@backRegister.route('/index/backendRegister',methods=['GET', 'POST'])
def backrgister():
    # if importPackage.request.method == 'POST':
    #     username = importPackage.request.form['username']
    #     password = importPackage.request.form['password']
    #     confirm_password = importPackage.request.form['confirm_password']
    #     if password != confirm_password:
    #         return "密碼比對錯誤，請重新輸入。"
    return importPackage.render_template('後台網頁/Back_register.html')
