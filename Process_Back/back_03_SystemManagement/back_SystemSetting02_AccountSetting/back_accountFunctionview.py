from publicUseFunction import importPackage, dbConnection
back_AccountFunctionView = importPackage.Blueprint(
    'back_AccountFunctionView', __name__)
back_AccountFunctionView.secret_key = 'abc'
conn = importPackage.conn


@back_AccountFunctionView.route('/backAccountFunctionView', methods=['GET', 'POST'])
def backAccountFunctionView():

    user = importPackage.session['user_id']
    current_time = importPackage.datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d")

    return importPackage.render_template('後台網頁/back_03_System_Management/back_02_AccountSetting/back_accountFunctionView.html', Handler=user, DateTime=formatted_time)
