from publicUseFunction import importPackage, dbConnection
from Process_Front.front_01_MainWebsite.front_login import get_user
from Process_BackFunction.Process_BackFunctionSelect import select_backNewSetting
front_Index = importPackage.Blueprint('front_Index', __name__)
front_Index.secret_key = 'abc'

conn = importPackage.conn
@front_Index.route('/')
@front_Index.route('/index')
def frontIndex():
    cursor = conn.cursor()
    cursor.execute(""" select "inputTitle","UploadTime" from "back_NewsSetting" """)
    result = cursor.fetchall()
    if 'user_id' in importPackage.session:
        user = importPackage.session['user_id']
        return importPackage.render_template('前台網頁/front_01_MainWebsite/front_index.html', user=user,result=result)
    else:
        return importPackage.render_template('前台網頁/front_01_MainWebsite/front_index.html', user=None,result=result)
    backNewSetting = select_backNewSetting()
    return importPackage.render_template('前台網頁/front_01_MainWebsite/front_index.html', result=backNewSetting)


@front_Index.route('/logout')
def logout():
    if 'user_id' in importPackage.session:
        del importPackage.session['user_id']
    return importPackage.redirect(importPackage.url_for('front_Index.frontIndex'))
