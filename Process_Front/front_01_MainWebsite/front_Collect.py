from publicUseFunction import importPackage, dbConnection
front_Collect = importPackage.Blueprint(
    'main_Collect', __name__)
front_Collect.secret_key = 'abc'

@front_Collect.route('/frontCollect')
def index():
    return importPackage.render_template('前台網頁/front_01_MainWebSite/front_Collect.html')
